## DSGP 2 -- Improvements to the argument syntax

| Author        | Author email         | Status   |
|---------------|----------------------|----------|
| Diego Ramirez | dr01191115@gmail.com | Approved |

## Overview

DiddiScript is mostly made with functions, that make several jobs and interactions with variables. However, at least before
this DSGP, functions only accept one parameter (or nothing):

```
!# ---- OLD DIDDISCRIPT FUNCTIONS BEHAVIOR ----

func1("some argument");  !# good
func2();                 !# good
func3("x", "y");         !# wrong
```

This DSGP proposes the idea of multiple arguments, so the following code would become valid:

```
func3("x", "y");
```

## The old argument syntax vs. the new syntax

### Old syntax

The old syntax is based on the first DiddiScript parser, [DiddiParser][1]. It is a bit basic, and can be explained like this:

```
[function name]([optional quoted argument]);
```

This syntax only allows one quoted argument. In some cases, this is very effective. But in many other cases, this
syntax is useless in the practice.

### New syntax

The proposed syntax is a bit more complicated:

```
[function name]([variables, values or text]);
```

In the `variables, values or text` space, an infinite number of arguments can be passed, or also none arguments. Each function
can sketch how many arguments will be accepted. The parser only has to pass all the arguments, and the function will make the rest.

Another proposed approach of this new syntax is allowing to **use variables directly**, not just like text indexes. Their true type will
be used, instead of a text copy.

Also, **non-stored values** would be passed as arguments. This behavior was "present" before (all the arguments were non-stored texts), but now
all the values defined in [DSGP 1][2] (and any other accepted DSGP in the future) will be allowed.

The previous behavior would also be possible, we are only refactoring how the parser should understand the arguments.

## Examples

Direct usage of variables:

```
var x = 15

func(x);
```

Non-stored values:

```
!# Using types from DSGP 1
func(True);
func(2.3);
func(23);
func(Null);
func("Some text");
```

Multiple arguments:

```
var x = 23.4;
var y = 12.56;

func("Some text", x, y, Null, False);
```

## Considerations

### Passing the arguments to the function

Like we described above:

> The parser only has to pass all the arguments, and the function will make the rest.

The functions can define all the variables as needed. Some of them can be optional, but there's
a fundamental rule: **they should be positional arguments, not keyword arguments**.

This DSGP hasn't considered the option of having keyword arguments. However, the idea can be taken
without problems by another DSGP.

[1]: https://github.com/DiddiLeija/diddiparser
[2]: https://github.com/DiddiLeija/diddiparser2/blob/main/dsgp/dsgp-1.md
