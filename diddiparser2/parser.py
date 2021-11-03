"""
DiddiScript main parser.
"""

import importlib
import io
import sys

from diddiparser2.messages import compile_error, show_warning, success_message

__version__ = "1.0.0"

TOOL_FUNCTIONS = ["load_module"]
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

    def executeline(self, line):
        "Parse, read and run a single line of code."
        line = line.replace('("', "(")
        line = line.replace("('", "(")
        line = line.replace('")', ")")
        line = line.replace("')", ")")
        parsed_line = line.replace(");", "")
        call, arg = parsed_line.split("(")[0], parsed_line.split("(")[1]
        if call == "load_module":
            mod = importlib.import_module(f"diddiparser2.lib.{arg}")
            mod_list = mod.DIDDISCRIPT_FUNCTIONS
            for item in mod_list:
                exec(f"from diddiparser2.lib.{arg} import {item} as element; MODULE_FUNCTIONS['{item}'] = element", locals(), globals())
        elif call in MODULE_FUNCTIONS.keys():
            func = MODULE_FUNCTIONS[call]
            func(arg)
        else:
            compile_error(f"No such function '{call}'")
