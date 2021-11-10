"""
DiddiScript main parser.
"""

import importlib
import io
import sys

from diddiparser2.messages import compile_error
from diddiparser2.messages import error as messages_error
from diddiparser2.messages import show_command, show_warning, success_message

__version__ = "1.0.0"

TOOL_FUNCTIONS = ["load_module", "load_extension"]
MODULE_FUNCTIONS = dict()


class DiddiParser:
    """
    Main class of the DiddiScript
    parser.
    """

    def __init__(self, file, strategy=io.open, ignore_suffix=False):
        "Constructor method."
        if not file.endswith(".diddi") and not ignore_suffix:
            show_warning(
                f"The invocation file '{file}' is not recognized as"
                "a DiddiScript file ('*.diddi'). This may cause conflicts."
                " To override this warning, use 'ignore_suffix' (on Python"
                " code) or add the --ignore-suffix flag to the CLI."
            )
        self.script = strategy(file)
        self.commands = self.get_commands()

    def get_commands(self):
        "Get the commands from our script."
        seq = []
        for line in self.script:
            # remove inline comments
            line = line.split("!#")[0].strip()
            if not line.endswith(";"):
                compile_error("Missing semicolon (;) at the end of the line")
            seq.append(line)
        return seq

    def runfile(self):
        "Run the parsed file."
        for line in self.commands:
            self.executeline(line)
            print("=" * 60)
        success_message()

    def print_command(self, cmd):
        "By default, we use the fancy `messages.show_command`"
        # Show the command
        show_command(cmd)

    def executeline(self, line):
        "Parse, read and run a single line of code."
        line = line.replace('("', "(")
        line = line.replace("('", "(")
        line = line.replace('")', ")")
        line = line.replace("')", ")")
        parsed_line = line.replace(");", "")
        call, arg = parsed_line.split("(")[0], parsed_line.split("(")[1]
        self.print_command(f"{call}({arg})")
        if call not in MODULE_FUNCTIONS and call not in TOOL_FUNCTIONS:
            compile_error(f"No such function '{call}'")
        if call == "load_module":
            mod = importlib.import_module(f"diddiparser2.lib.{arg}")
            mod_list = mod.DIDDISCRIPT_FUNCTIONS
            for item in mod_list:
                exec(
                    f"from diddiparser2.lib.{arg} import {item} as element; MODULE_FUNCTIONS['{item}'] = element",
                    locals(),
                    globals(),
                )
        if call == "load_extension":
            # Two things are allowed here:
            # 1. A Python-like import: "pkg.module" | "module"
            # 2. A rough Python file: "module.py"
            if arg.endswith(".py"):
                arg = arg.replace(".py", "")
            ext = importlib.import_module(f"{arg}")
            ext_list = ext.DIDDISCRIPT_FUNCTIONS
            for item in ext_list:
                exec(
                    f"from {arg} import {item} as element; MODULE_FUNCTIONS['{item}'] = element",
                    locals(),
                    globals(),
                )
        if call in MODULE_FUNCTIONS.keys():
            func = MODULE_FUNCTIONS[call]
            func(arg)


class InteractiveDiddiParser(DiddiParser):
    "A fancy console, to run DiddiScript commands."
    intro = f"""
Welcome to the interactive DiddiParser console.
Parser version: {__version__}
{'='*60}
"""

    def __init__(self):
        pass

    def loop(self):
        "Generate an interactive console."
        print(self.intro)
        while 1:
            # get the "command"
            try:
                self.script = [input("> ")]
            except EOFError:
                sys.exit(0)
            except KeyboardInterrupt:
                print("\nKeyboardInterrupt")
                continue
            # compile and run
            try:
                line = self.get_commands()[0]
                if line.strip() != "":
                    self.executeline(line)
            except messages_error as exc:
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
