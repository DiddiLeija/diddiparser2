"""
The DiddiScript main parser. This tool
is written in Python and distributed as
a package on PyPI (https://pypi.org).

Its main feature is a CLI tool to run
DiddiScript files. Also, it has a CLI for
an interactive console. And it has a
code editor focused on DiddiScript.
"""

import importlib
import io
import os
import sys

from diddiparser2 import messages
from diddiparser2.diddiscript_types import Boolean, Floating, Integer, Null, Text
from diddiparser2.messages import compile_error
from diddiparser2.messages import error as DSError
from diddiparser2.messages import show_command, show_warning, success_message

__version__ = "1.0.0"

TOOL_FUNCTIONS = [
    "load_module",
    "load_extension",
    "print_available_functions",
    "chdir",
    "cd",
    "store_last_value",
]
MODULE_FUNCTIONS = dict()
EXECUTION_VARIABLES = dict()


def remove_item_from_dict(seq, item):
    "Remove `item` from dictionary `seq`."
    copy = dict()
    for k, v in seq.items():
        if k == item:
            continue
        copy[k] = v
    return copy


class DiddiParser:
    """
    Main class of the DiddiScript
    parser.
    """

    last_value = None

    def __init__(
        self,
        file,
        strategy=io.open,
        ignore_suffix=False,
        verbose=False,
        compile_only=False,
        notify_success=True,
    ):
        "Constructor method."
        if not file.endswith(".diddi") and not ignore_suffix:
            show_warning(
                f"The invocation file '{file}' is not recognized as "
                "a DiddiScript file ('*.diddi'). This may cause conflicts. "
                "To override this warning, use 'ignore_suffix' (on Python "
                "code) or add the --ignore-suffix flag to the CLI. "
            )
        self.script = strategy(file)
        self.commands = self.get_commands()
        self.verbose = verbose
        self.compile_only = compile_only
        self.notify_success = notify_success

    def identify_value(self, value, from_func=False):
        "Identify the true value of a variable."
        if type(value) in (Null, Boolean, Text, Floating, Integer):
            return value
        elif not isinstance(value, str):
            # We need strings to modify this
            compile_error(f"fatal: expected string as initial value, but got {value}")
        value = value.strip()
        if "'" in value or '"' in value:
            # A piece of text, just return
            if value == "''" or value == '""':
                return Text("")
            return Text(self.parse_string_indexing(value[1:-1]))
        elif value in ("True", "False"):
            # A boolean
            return Boolean(value)
        elif value == "Null":
            # An empty space
            return Null()
        else:
            # The last possible values are
            # floats and integers
            try:
                if "." in value:
                    # A floating number
                    return Floating(value.strip())
                # Maybe an integer?
                return Integer(value.strip())
            except Exception:
                # It failed, so we raise an error
                if from_func:
                    # This is a workaround to
                    # https://github.com/DiddiLeija/diddiparser2/issues/43.
                    # We will return a Text object, but we will warn the user.
                    show_warning(
                        f"We could not identify this value returned by a function: {value}. "
                        "We will convert it to rough text. Please see "
                        "https://github.com/DiddiLeija/diddiparser2/issues/43 for more details."
                    )
                compile_error(f"Could not identify value: {value}")

    def get_commands(self):
        "Get the commands from our script."
        seq = []
        for line in self.script:
            # remove inline comments
            line = line.split("!#")[0].strip()
            if len(line) > 0:
                if not line.endswith(";"):
                    compile_error("Missing semicolon (;) at the end of the line")
                seq.append(line)
        return seq

    def runfile(self):
        "Run the parsed file."
        for line in self.commands:
            if self.verbose:
                # Verbose mode, so we should
                # print the command introduced
                self.print_command(line)
            self.executeline(line)
        if self.notify_success:
            if not self.compile_only:
                success_message()
            else:
                success_message("The compilation was succesfull!")

    def print_command(self, cmd):
        "By default, we use the fancy `messages.show_command`"
        # Show the command
        show_command(cmd)

    def executeline(self, line):
        "Execute something on each line."
        if line.lstrip().startswith("var "):
            self.execute_def(line)
        else:
            self.execute_func(line)

    def execute_def(self, line):
        "Define a variable."
        line = line.lstrip()[4:-1]
        if "=" not in line:
            # A single-line variable, default to DSGP 1's Null
            EXECUTION_VARIABLES[line.strip()] = Null()
            return None  # cut before anything else
        parsed_line = line.split("=")
        name = parsed_line[0].rstrip()
        value = parsed_line[1].lstrip()
        if name in TOOL_FUNCTIONS:
            show_warning(
                f"The variable name '{name}' is overwriting an existing tool "
                "function. Since now, that function will be unavailable."
            )
            TOOL_FUNCTIONS.remove(name)
        elif name in MODULE_FUNCTIONS.keys():
            show_warning(
                f"You are overwriting a function named '{name}' with a variable. "
                "Now, that function is unavailable."
            )
            remove_item_from_dict(MODULE_FUNCTIONS, name)
        value = self.identify_value(value)
        EXECUTION_VARIABLES[name] = value

    def parse_string_indexing(self, text):
        """
        Replace indexes in text with true variables.
        By default, this uses the DSGP 1 specification
        (`${variable}`).
        """
        aux = text.split("${")
        final_line = text.split("${")[0] if not text.startswith("${") else ""
        for piece in aux[1:]:
            index = piece.split("}")
            if len(index) != 2:
                index = (index[0], "")
            if index[0] not in EXECUTION_VARIABLES.keys():
                compile_error(f"Could not resolve variable reference: {index[0]}")
            true_value = EXECUTION_VARIABLES[index[0]]
            final_line = f"{final_line}{true_value}{index[1]}"
        return final_line

    def resolve_value_or_variable(self, arg):
        """
        This resolves between direct values or variables
        using the DSGP 2 specification.
        """
        if arg in EXECUTION_VARIABLES.keys():
            return EXECUTION_VARIABLES[arg]
        return self.identify_value(arg)

    def execute_func(self, line):
        "Run a call(argument) function."
        parsed_line = line.replace(");", "")
        call = parsed_line.split("(")[0]
        pos = len(f"{call}(")  # use this to avoid conflicts
        args_aux = parsed_line[pos:]
        args_aux = args_aux.split(",")
        last_piece = ""
        args = []
        for piece in args_aux:
            counter = None
            if "'" in piece:
                counter = 0
                for char in piece:
                    counter += 1 if char == "'" else 0
            if '"' in piece:
                counter = 0
                for char in piece:
                    counter += 1 if char == '"' else 0
            if counter is not None:
                if counter < 2 and (
                    piece.strip().endswith("'") or piece.strip().endswith('"')
                ):
                    piece = last_piece + "," + piece
                    args.pop()
            last_piece = piece
            args.append(piece)
        fixed_args = []
        del pos, args_aux, last_piece  # delete the aux
        for arg in args:
            if arg != "":
                arg = self.resolve_value_or_variable(arg)
                fixed_args.append(arg)
        if call in MODULE_FUNCTIONS.keys():
            func = MODULE_FUNCTIONS[call]
            try:
                if not self.compile_only:
                    value = func(*fixed_args)
                    if value is not None:
                        self.last_value = self.identify_value(value, from_func=True)
                    else:
                        self.last_value = Null()
                return None
            except DSError:
                # we *should* fail here
                raise
            except Exception:
                self.last_value = Null()
        elif call == "cd" or call == "chdir":
            if self.compile_only:
                return None
            os.chdir(str(fixed_args[0]))
            self.last_value = fixed_args[0]
        elif call == "load_module":
            mod = importlib.import_module(f"diddiparser2.lib.{fixed_args[0]}")
            mod_list = mod.DIDDISCRIPT_FUNCTIONS
            for item in mod_list:
                if item in TOOL_FUNCTIONS:
                    show_warning(
                        f"The '{item}' special function is being overridden. "
                        "This may cause issues, or even make the parser to be useless."
                    )
                exec(
                    f"from diddiparser2.lib.{fixed_args[0]} import {item} as element; MODULE_FUNCTIONS['{item}'] = element",
                    locals(),
                    globals(),
                )
            self.last_value = Null()
        elif call == "load_extension":
            # A Python-like import is expected. For
            # example: "module", "pkg.module"
            ext = importlib.import_module(f"{fixed_args[0]}")
            ext_list = ext.DIDDISCRIPT_FUNCTIONS
            for item in ext_list:
                if item in TOOL_FUNCTIONS:
                    show_warning(
                        f"The '{item}' special function is being overridden. "
                        "This may cause issues, or even make the parser to be useless."
                    )
                exec(
                    f"from {fixed_args[0]} import {item} as element; MODULE_FUNCTIONS['{item}'] = element",
                    locals(),
                    globals(),
                )
            self.last_value = Null()
        elif call == "print_available_functions":
            # Print the available functions
            if self.compile_only:
                return None
            if arg:
                show_warning("This function is not currently accepting arguments.")
            print("---- Special functions ----")
            for item in TOOL_FUNCTIONS:
                print(f"  {item}")
            print("---- Loaded functions ----")
            for item in MODULE_FUNCTIONS:
                print(f"  {item}")
            self.last_value = Null()
        elif call == "store_last_value":
            EXECUTION_VARIABLES[str(fixed_args[0])] = (
                self.last_value if self.last_value is not None else Null()
            )
        else:
            compile_error(f"No such function '{call}'")


class InteractiveDiddiParser(DiddiParser):
    "A fancy console, to run DiddiScript commands."
    intro = f"""
Welcome to the interactive DiddiParser console.
Parser version: {__version__}
{'='*60}
"""

    def __init__(self):
        self.compile_only = False
        self.verbose = False

    def loop(self):
        "Generate an interactive console."
        print(self.intro)
        while 1:
            # get the "command"
            try:
                self.script = [input("> ")]
                if len(self.script[0].strip()) < 1:
                    continue
            except EOFError:
                sys.exit(0)
            except KeyboardInterrupt:
                print("\nKeyboardInterrupt")
                continue
            # compile and run
            try:
                line = self.get_commands()[0]
                self.executeline(line)
            except messages.error as exc:
                # someone raised a DiddiParser
                # error... just don't crash!
                print(f"Error: {str(exc)}\n")

    def print_command(self, cmd):
        "Override this step."
        pass


def interactive_console():
    "Function used to generate the interactive console."
    console = InteractiveDiddiParser()
    console.loop()
