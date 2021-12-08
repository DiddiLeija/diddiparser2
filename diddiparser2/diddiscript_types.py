"""
Collector for the "standard variables" described by DSGP 1.
"""

from diddiparser2.messages import show_warning

__all__ = ("diddiscript_types_list")


class DiddiScriptType:
    "Template class."
    value = object()

    def __str__(self):
        return str(self.value)


class Integer(DiddiScriptType):
    "Integer, natural numbers."

    def __init__(self, value_text):
        self.value = int(value_text)


class Floating(DiddiScriptType):
    "Floating (decimal) numbers."

    def __init__(self, value_text):
        self.value = float(value_text)


class Text(DiddiScriptType):
    "Simple text."

    def __init__(self, value_text):
        self.value = value_text  # we expect this to be a string

    def __str__(self):
        return self.value


class Boolean(DiddiScriptType):
    "True or False."

    def __init__(self, value_text):
        if value_text in ("True", "False"):
            self.value = bool(value_text)
        else:
            # This weird expression will help us to
            # identify a "boolean value", even when it is incorrect.
            show_warning(
              f"No valid DiddiScript boolean values were found for '{value_text}'. "
              "A truthy-falsy result will be stored instead."
            )
            self.value = (not self.value) is False


class Null(DiddiScriptType):
    "Nothing to store here!"

    def __init__(self, value_text):
        # we won't care for 'value_text' now.
        self.value = None

    def __str__(self):
        return "Null"

diddiscript_types_list = (Integer, Floating, Text, Boolean, Null)
