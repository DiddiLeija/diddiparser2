## DSGP 3 -- The Ultimate extensions guide

| Author        | Author email         | Status   |
|---------------|----------------------|----------|
| Diego Ramirez | dr01191115@gmail.com | Approved |

## Overview

[DiddiParser 2][1] makes possible to extend the DiddiScript library via [extensions](https://diddiparser2.readthedocs.io/en/latest/language/load_extension.html), which
are, basically, importable Python files. This DSGP provides the ultimate guide and some standards of how to write the best extension.

## File ubications, names, etc.

First of all, you must write _all_ the extensions in valid Python files (`*.py`), like the DiddiScript standard libraries. To get sure they will work, they should be able to
be imported with Python at the working directory where DiddiScript will be executed. It is valid to write extensions inside a package living in the site packages, too.

The name rules are the same than those that apply on Python.

## Adding functions for DiddiScript

Now that you have a valid Python file, you will have to provide some stuff before making it a useful extension.

### The `DIDDISCRIPT_FUNCTIONS` variable

You have to define this to tell the parser which of the functions defined in the module should be used on DiddiScript. This variable is a sequence of strings.
Each string is a function name. The function must exist in the module.

### Function definitions

These are simple Python functions. They should accept, at least, one argument. However, they can have multiple arguments.

You should consider that your function will receive [DiddiScript types][2], which, in Python, are represented by [these Python types][3].
Use their `.value` attribute for getting the true value, almost represented by a known Python type.

The return value should be another [DiddiScript Python type][3], or just don't return anything. You could also pass strings, however, this is not a recommended behavior.

### Using the [DiddiParser 2][1] API

You can use these modules for simplifying your functions with convenience stuff used by DiddiScript:

- [`diddiparser2.diddiscript_types`][3] -- DiddiScript types as Python classes
- [`diddiparser2.messages`][4] -- Tools for interacting, showing errors, and more
- [The DiddiScript library at `diddiparser2.lib`][5] -- You can use these libraries for convenience operations.
  For example, use [`diddiparser2.lib.simpleio.print_text`][6] and [`diddiparser2.lib.simpleio.print_line`][7] for doing what the Python `print()` does.

## Example

This is an extension that will provide 2 DiddiScript functions:

```python
from diddiparser2.diddiscript_types import Null
from diddiparser2.messages import show_warning
from diddiparser2.lib.simpleio import print_line

DIDDISCRIPT_FUNCTIONS = ("my_func", "my_func2")

def my_func(some_arg):
    print_line(f"Hello! I received a {some_arg}")


def my_func2(*args):
    for arg in args:
        if isinstance(arg, Null):
            show_warning("Found a Null!")
        else:
            print_line(f"Found a {arg}!")


def my_func3():
    # This function won't be accesible for DiddiScript, though
    # it can be easily used by Python. This is because "my_func3"
    # is not in DIDDISCRIPT_FUNCTIONS.
    pass
```

Then, on a DiddiScript file in the same working directory:

```
load_module("simpleio");
load_extension("extension_file_name");  !# This loads the "extension_file_name.py" file

var some_text = "dummy text";
var number = 1;

my_func(some_text);
print_line("=====");
my_func2(number, some_text, True, Null, 0);
```

The desired output should be:

```
Hello! I received a dummy text
=====
Found a 1!
Found a dummy text!
Found a True!
WARNING: Found a Null!
Found a 0!
```

<!-- A few links below -->

[1]: https://github.com/DiddiLeija/diddiparser2
[2]: https://diddiparser2.readthedocs.io/en/latest/language/variables.html#list-of-allowed-types
[3]: https://diddiparser2.readthedocs.io/en/latest/reference.html#module-diddiparser2.diddiscript_types
[4]: https://diddiparser2.readthedocs.io/en/latest/reference.html#module-diddiparser2.messages
[5]: https://diddiparser2.readthedocs.io/en/latest/language/stdlib/index.html
[6]: https://diddiparser2.readthedocs.io/en/latest/language/stdlib/simpleio.html#print_text
[7]: https://diddiparser2.readthedocs.io/en/latest/language/stdlib/simpleio.html#print_line
