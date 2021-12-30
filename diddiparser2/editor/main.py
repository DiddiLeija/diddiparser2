import tkinter

from idlelib.textview import view_text

from diddiparser2 import __doc__ as diddiparser2_doc
from diddiparser2.editor.menu import generate_menu
from diddiparser2.parser import __doc__ as diddiscript_doc


class DiddiScriptEditor:
    "Base class for the editor."

    def __init__(self):
        self.root = tkinter.Tk()
        self.file = None
        self.options = {
            "About": {
                "About DiddiScript": lambda: view_text(
                    self.root, "About DiddiScript", diddiscript_doc
                ),
                "About DiddiParser 2": lambda: view_text(
                    self.root, "About DiddiParser 2", diddiparser2_doc
                ),
            }
        }
        self.startsetup()

    def startsetup(self):
        "Generate an initial interface, and work on it."
        self.editor_frame = tkinter.Frame(self.root)
        # NOTE: We used grid() for personal reasons. We
        #       should try to move over to pack() in the
        #       near future.
        self.editor_frame.grid()
        self.menu = generate_menu(self.root, self.options)
