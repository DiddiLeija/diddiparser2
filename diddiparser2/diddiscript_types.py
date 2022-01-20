"""
Collector for the "standard variables" described by DSGP 1.
"""

from diddiparser2.messages import run_error, show_warning

__all__ = ["diddiscript_types_list"]


class DiddiScriptType:
    "Template class."
    value = object()

    def __str__(self):
        return str(self.value)

    def __int__(self):
        try:
            return int(self.value)
        except ValueError:
            run_error(
                f"Error: Could not return int from type: {type(self.value).__name__}"
            )

    def __float__(self):
        try:
            return float(self.value)
        except ValueError:
            run_error(
                f"Error: Could not return float from type: {type(self.value).__name__}"
            )

    def __bool__(self):
        return bool(self.value)


class Integer(DiddiScriptType):
    "Integer, natural numbers."

    def __init__(self, value_text):
        self.value = int(value_text)

    def __int__(self):
        return self.value


class Floating(DiddiScriptType):
    "Floating (decimal) numbers."

    def __init__(self, value_text):
        self.value = float(value_text)

    def __float__(self):
        return self.value


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
            # Tell the user that this is wrong
            show_warning(
                f"No valid DiddiScript boolean values were found for '{value_text}'. "
                "A truthy-falsy result will be stored instead."
            )
            # This weird expression will help us to
            # identify a "boolean value", even when it is incorrect.
            self.value = (not self.value) is False

    def __bool__(self):
        return self.value


class Null(DiddiScriptType):
    "Nothing to store here!"

    def __init__(self, value_text=None):
        # we won't care for 'value_text' now.
        self.value = None

    def __str__(self):
        return "Null"


diddiscript_types_list = {
    "int": Integer,
    "float": Floating,
    "str": Text,
    "bool": Boolean,
    "None": Null,
}

for ds_type in diddiscript_types_list.values():
    __all__.append(ds_type)
