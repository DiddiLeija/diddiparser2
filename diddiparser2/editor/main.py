import tkinter
from tkinter import TclError, filedialog, messagebox

from idlelib.textview import view_text

from diddiparser2 import __doc__ as diddiparser2_doc
from diddiparser2.editor import __doc__ as editor_doc
from diddiparser2.messages import error as DSError
from diddiparser2.messages import success_message
from diddiparser2.parser import DiddiParser
from diddiparser2.parser import __doc__ as diddiscript_doc


def format_exception(exc):
    if isinstance(exc, TclError):
        msg = f"Tcl Error: {str(exc)}"
    elif not hasattr(type(exc), "__name__"):
        msg = str(exc)
    else:
        msg = f"{type(exc.__name__)}: {str(exc)}"
    return msg


def is_func(line):
    return "(" in line and ")" in line and not line.startswith("(")


def is_vardef(line):
    return "var" in line and line.startswith("var ")


def compile_diddiscript(text, parse_method, verbose, just_compile=False):
    "Compile DiddiScript using a Text widget."
    try:
        line_index = 0
        parser = DiddiParser(
            text,
            strategy=parse_method,
            ignore_suffix=True,
            verbose=verbose,
            compile_only=just_compile,
            notify_success=False,
        )
        # Now we emulate parser.runfile, but
        # introducing the line count and removing
        # the success record...
        for line in parser.commands:
            line_index += 1
            if verbose:
                parser.print_command(line)
            parser.executeline(line)
        if not just_compile:
            success_message()
        else:
            success_message("The compilation was succesfull!")
        print("=" * 60)
    except DSError:
        print("=" * 60)
        raise Exception(
            f"Error, at line {line_index}: found an undefined name or syntax error."
        )


def generate_menu(root, options):
    """
    Generate a menu from a Tk window and
    a list of dictionaries with options.
    """
    main_menu = tkinter.Menu(root)
    for name in options:
        # BUG: It seems like the `options` cannot be
        #      unpacked by .values(). Not sure why,
        #      but in the meantime, there's a
        #      workaround below:
        option = options[name]
        child_menu = tkinter.Menu(main_menu, tearoff=0)
        for label in option:
            # BUG: It seems like `option` cannot be
            #      unpacked by .values(). Not sure why,
            #      but in the meantime, there's a
            #      workaround below:
            command = option[label]
            child_menu.add_command(label=label, command=command)
        main_menu.add_cascade(label=name, menu=child_menu)
    root.config(menu=main_menu)


class DiddiScriptEditor:
    "Base class for the editor."

    def __init__(self):
        self.root = tkinter.Tk()
        self.file = None
        self.file_saved = False
        self.verbose = False
        self.ignore_suffix = False
        self.ftypes = [("DiddiScript file", "*.diddi"), ("All types", "*")]
        self.options = {
            "About...": {
                "About DiddiScript": lambda: view_text(
                    self.root, "About DiddiScript", diddiscript_doc
                ),
                "About DiddiParser 2": lambda: view_text(
                    self.root, "About DiddiParser 2", diddiparser2_doc
                ),
                "About this editor": lambda: view_text(
                    self.root, "About this editor", editor_doc
                ),
            },
            "File...": {
                "Save As...": self.save_file,
                "Save": self.save_new,
                "Open...": self.open_file,
            },
            "Run...": {"Compile code": self.compile_code, "Run code": self.run_code},
            "Settings": {
                "Set verbosity mode": self.set_verbosity,
                "Set suffix ignoring": self.set_suffix_ignoring,
            },
        }
        self.startsetup()

    def set_title(self):
        "Format and set the title of the Tk root."
        open_file = self.file is not None
        file_display = f" -- {self.file}"
        self.root.title(f"DiddiScript Editor{file_display if open_file else ''}")

    def startsetup(self):
        "Generate an initial interface, and work on it."
        self.set_title()
        self.editor_frame = tkinter.Frame(self.root)
        # NOTE: We used grid() for personal reasons. We
        #       should try to move over to pack().
        self.editor_frame.grid()
        self.menu = generate_menu(self.root, self.options)
        self.text_entry = tkinter.Text(self.root)
        self.text_entry.grid(row=0, column=0, sticky="ew")

    def save_file(self, save_new=True):
        if save_new:
            to_save = filedialog.asksaveasfilename(
                parent=self.root, filetypes=self.ftypes
            ).strip()
        else:
            to_save = self.file.strip()
        if len(to_save) < 1:
            messagebox.showinfo("No file selected", "You didn't select a file to save.")
            return None
        try:
            with open(to_save, "w") as f:
                f.write(str(self.text_entry.get("1.0", "end")) + "\n")
        except Exception as exc:
            msg = format_exception(exc)
            messagebox.showerror(
                "Error while saving",
                f"""Fatal: Failed to save file {to_save}.

Error: \"{msg}\" """,
            )
        self.file = to_save
        self.set_title()

    def save_new(self):
        if self.file is None:
            self.save_file()
        else:
            self.save_file(False)

    def open_file(self):
        to_open = filedialog.askopenfilename(
            parent=self.root, filetypes=self.ftypes
        ).strip()
        if len(to_open) < 1:
            messagebox.showinfo("No file selected", "You didn't select a file to open.")
            return None
        try:
            if not to_open.endswith(".diddi") and not self.ignore_suffix:
                messagebox.showwarning(
                    "Suffix warning",
                    """Warning! The selected file does not end with '*.diddi'.
Maybe you selected the wrong file, and its syntax may not work.

To supress the warning, go to 'Settings' > 'Set verbosity'.""",
                )
            with open(to_open, "r") as f:
                chars = f.read()
        except Exception as exc:
            msg = format_exception(exc)
            messagebox.showerror(
                "Error while opening",
                f"""Fatal: Failed to open file {to_open}.

Error: \"{msg}\" """,
            )
        self.file = to_open
        self.text_entry.delete("1.0", "end")
        self.text_entry.insert("1.0", chars)
        self.set_title()

    def compile_code(self):
        def get_lines(text):
            return text.splitlines()

        code = str(self.text_entry.get("1.0", "end"))
        try:
            compile_diddiscript(code, get_lines, self.verbose, True)
            messagebox.showinfo("Compilation completed", "Everything looks good!")
        except Exception as exc:
            messagebox.showerror("Compilation failed", str(exc))

    def run_code(self):
        def get_lines(text):
            return text.splitlines()

        code = str(self.text_entry.get("1.0", "end"))
        try:
            compile_diddiscript(code, get_lines, self.verbose, False)
            messagebox.showinfo(
                "Process completed", "The execution finished succesfully!"
            )
        except Exception as exc:
            messagebox.showerror(
                "Process failed",
                f"""Something went wrong while compiling/running at line {str(exc).split()[3][:-1]}.
To check for compiling issues (undefined names, syntax errors),
go to 'Run' > 'Compile code'.""",
            )

    def set_verbosity(self):
        entry = messagebox.askyesno(
            "Set verbosity?",
            f"""Do you want to run DiddiScript in verbose mode?
Current setting: {self.verbose}.""",
        )
        if entry is True:
            self.verbose = True
        elif entry is False:
            self.verbose = False
        else:
            messagebox.showwarning(
                "Nothing selected",
                "We could not identify a valid input. " "The setting hasn't changed.",
            )

    def set_suffix_ignoring(self):
        entry = messagebox.askyesno(
            "Set suffix ignoring?",
            f"""Do you prefer to ignore the file suffix on files?
If True, this editor won't warn you when a file does not have the '*.diddi' suffix.
Current setting: {self.ignore_suffix}.""",
        )
        if entry is True:
            self.ignore_suffix = True
        elif entry is False:
            self.ignore_suffix = False
        else:
            messagebox.showwarning(
                "Nothing selected",
                "We could not identify a valid input. " "The setting hasn't changed.",
            )


def main():
    editor = DiddiScriptEditor()
    editor.root.mainloop()


if __name__ == "__main__":
    main()
