import tkinter
from idlelib.textview import view_text
from tkinter import TclError, filedialog, messagebox, scrolledtext

from diddiparser2 import __doc__ as diddiparser2_doc
from diddiparser2.editor import __doc__ as editor_doc
from diddiparser2.editor import formatter
from diddiparser2.messages import error as DSError
from diddiparser2.messages import success_message
from diddiparser2.parser import DiddiParser
from diddiparser2.parser import __doc__ as diddiscript_doc


def format_exception(exc):
    if isinstance(exc, TclError):
        return f"Tcl Error: {str(exc)}"
    return f"{type(exc).__name__}: {str(exc)}"


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
    for name, option in options.items():
        child_menu = tkinter.Menu(main_menu, tearoff=0)
        for label, command in option.items():
            if not isinstance(command, dict):
                child_menu.add_command(label=label, command=command)
            else:
                # Multiple options are inside, it's time to
                # generate a sub-menu.
                submenu = tkinter.Menu(child_menu, tearoff=0)
                for sub_label, sub_cmd in command.items():
                    submenu.add_command(label=sub_label, command=sub_cmd)
                child_menu.add_cascade(label=label, menu=submenu)
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
                "New file": self.new_file,
                "Save As...": self.save_file,
                "Save": self.save_new,
                "Open...": self.open_file,
            },
            "Run...": {"Compile code": self.compile_code, "Run code": self.run_code},
            "Settings": {
                "Set verbosity mode": self.set_verbosity,
                "Set suffix ignoring": self.set_suffix_ignoring,
            },
            "Themes": {
                "Load themes from JSON file": self.json_theme,
                "See all the themes": self.show_themes,
                "Set theme": {
                    # Some basic themes below, but others may join the list
                    "Light DiddiScript": lambda: self.set_theme("Light DiddiScript"),
                    "Dark DiddiScript": lambda: self.set_theme("Dark DiddiScript"),
                },
            },
        }
        self.startsetup()
        self.set_theme("Light DiddiScript")

    def set_title(self):
        "Format and set the title of the Tk root."
        open_file = self.file is not None
        file_display = f" -- {self.file}"
        self.root.title(f"DiddiScript Editor{file_display if open_file else ''}")

    def startsetup(self):
        "Generate an initial interface, and work on it."
        self.set_title()
        self.editor_frame = tkinter.Frame(self.root)
        self.editor_frame.pack(expand=True)
        self.menu = generate_menu(self.root, self.options)
        self.text_entry = scrolledtext.ScrolledText(self.editor_frame)
        self.text_entry.pack(expand=True)

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
                code_to_save = str(self.text_entry.get("1.0", "end")) + "\n"
                code_to_save = code_to_save.rstrip() + "\n"
                f.write(code_to_save)
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

    def new_file(self):
        if len(self.text_entry.get("1.0", "end").strip()) > 0:
            # Something is in the Text widget, so we may wanna
            # save it. Anyway, we have to ask.
            decision = messagebox.askyesnocancel(
                "Want to save the file?",
                "If you haven't saved yet, "
                "the moment is now. "
                "To save, press 'Yes'. "
                "To avoid saving, press 'No'. "
                "To cancel, just press 'Cancel'.",
            )
        else:
            # Seems like there's no reason to deal with
            # "save or not save" dilemmas, just set "decision"
            # to False. Maybe the newlines added will die after that,
            # though.
            #
            # NOTE: Should we set "decision" to None instead
            #       of False?
            decision = False
        # According to the user's input, move around
        if decision is True:
            # Save and open new
            self.save_new()
            self.file = None
            self.text_entry.delete("1.0", "end")
        elif decision is False:
            # Don't save, and open new
            self.file = None
            self.text_entry.delete("1.0", "end")
        else:
            # Don't do anything. Also, skip the
            # title manipulation below.
            return None
        # Since the "file" information might have changed.
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
                "We could not identify a valid input. The setting hasn't changed.",
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
                "We could not identify a valid input. The setting hasn't changed.",
            )

    def json_theme(self):
        file = filedialog.askopenfilename(
            parent=self.root, filetypes=[("JSON file", "*.json"), ("All types", "*")]
        )
        formatter.load_json_theme(file, self.refresh_themes_menu)

    def show_themes(self):
        view_text(self.root, "Available themes", formatter.format_themes())

    def set_theme(self, name):
        formatter.format_text(self.text_entry, name)

    def refresh_themes_menu(self, name=None):
        if name is None:
            # This might be some kind of "legacy way"
            # to update everything, though it was given me
            # several issues, so I replaced it with another
            # strategy, which resolves the issue.
            for key in formatter.THEMES.keys():
                if key not in self.options["Themes"]["Set theme"].keys():
                    self.options["Themes"]["Set theme"][key] = lambda: self.set_theme(
                        key
                    )
        else:
            self.options["Themes"]["Set theme"][name] = lambda: self.set_theme(name)
        self.menu = generate_menu(self.root, self.options)


def main():
    editor = DiddiScriptEditor()
    editor.root.mainloop()


if __name__ == "__main__":
    main()
