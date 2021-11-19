# DSGP 1 -- Variable definition

| Author        | Author email         | Status   |
|---------------|----------------------|----------|
| Diego Ramirez | dr01191115@gmail.com | Pending  |

## Overview

DiddiScript can handle functions with a single argument. However, they can
only be rough strings, or text:

```
func("arg");
```

This DSGP proposes the idea of handling variables for using them on functions.

## Defining variables

The variables should be defined with a `var` keyword, followed by a `=` operator, and
the value stored on it. Like the functions, this line should end with a `;`.
The variables should be stored on a sequence of type `name: value`, separated from the parser's variables.

## Allowed variable types

- **Integers:** Natural and real numbers, positive or negative.
- **Floats:** Floating, real numbers.
- **Text:** Quoted text, encoded.
- **Boolean:** True or False.
- **Null:** Nothing to store. Defined by default, if the variable has no "value".

The parser should have trouble to understand which type is each variable, so it would not
be necessary to say which type is stored.


## Saving last value returned by a function into a variable

This DSGP introduces the `store_last_value` special function. The design of the function will let
to create a variable (or overwrite an existing one) with the last value returned by a function.

```
var result;  !# An empty variable

some_func_with_return_value("...");

store_last_value("result");  !# Its argument should be a string refering to the variable

other_function("${result}");  !# Use the variable
```

## Usage as function arguments

This DSGP proposes two ideas:

1. **Using the variables as independent arguments.** Something like `func(x)`.
2. **Using _string indexing_ only.** To do that kind of markup, this DSGP proposes `func("I have !{x}")` (like other languages' indexes)

## Examples

To define a variable:

```
var v;                   !# null
var w = True;            !# boolean
var x = "Hello world!";  !# text
var y = 123;             !# integer
var z = 123.456;         !# float
```

Using them under functions:

```
var x = "pizza";

func(x);              !# idea 1
func("I love ${x}");  !# idea 2
```

## Considerations

### Overwriting variables with other variables

It should be possible to change the value, and even the type of a variable, by running the
`var` keyword again, defining the same variable.

### Overwriting a function with a variable

It would be possible to overwrite the name of a function with a variable. However, the parser has the
responsibility of warning the user. After the overwriting, the function won't be accessible, and the
variable will take its place.

### Creating custom types

This DSGP is not considering custom variable types. Only the types described above are considered.
However, this idea can be taken in a future DSGP, or even replace this scheme.
