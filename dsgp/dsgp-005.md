# DSGP 5 -- First statements

| Author        | Author email         | Status   |
|---------------|----------------------|----------|
| Diego Ramirez | dr01191115@gmail.com | Pending  |

## Overview

In the 1.x series of [DiddiParser 2][1], having statements was just impossible, unless
you figured out a way using functions.

But after [DSGP 4][2] acceptance, there's a chance for a new feature of the DiddiScript syntax:
**statements**. However, that DSGP didn't define any statement, it only defined the concept.

This DSGP is the DSGP 4 partner, and defines the first bunch of statements, which are statements
accepted by several languages.

## The `if/elseif/else` statements

The `if/elseif/else` can be easily recognized, because multiple languages accept the `if/else`
structure, and many of them have the `elseif` as the something-in-between (in other languages,
`elseif` is also known as `elif` or `else if`).

The syntax, based in the DSGP 4 syntax, goes as follows:

```
if (boolean) {
    !# steps
}
elseif (boolean) {
    !# steps
}
else {
    !# steps
}
```

Since it is a set of dependent statements, they should combine to achieve certain goals.
The following marked combinations are allowed. Unmarked combinations are considered syntax errors:

- [x] `if`
- [x] `if` / `else`
- [x] `if` / multiple `elseif`s
- [x] `if` / multiple `elseif`s / `else`
- [ ] multiple `elseif`s
- [ ] `else`
- [ ] multiple `elseif`s / else
- [ ] `if` / statements different than `if/elseif/else` / `else`
- [ ] statements different than `if/elseif/else` / `else`
- [ ] statements different than `if/elseif/else` / `elseif`

First of all, there should be one `if` (no orphan `elseif` or `else` blocks are allowed).
There shuld be one `else` block (or none). An infinite number of `elseif` blocks are allowed.

## The `while` statement

The `while` statement is another well-accepted loop. It repeats the nested steps while the
condition is true. The syntax is the following:

```
while (boolean) {
    !# steps
}
```

The way conditions are evaluated is:

- Check the condition
  - If true, run the nested steps.
  - If false, break the loop.

The flow can be affected by `break` and `continue` instructions (see below). Infinite loops can
happen (if the condition doesn't change and keeps true).

## The `repeat` statement

The `repeat` statement will repeat steps.

Unlike `while`, `repeat` won't analyze a condition. Instead, it will repeat the steps for a strict
number of steps (integer or floating numbers are expected). For example, if `10` is passed, the
steps will be repeated 10 times.

This is the syntax:

```
repeat (integer_or_floating) {
    !# steps
}
```

The flow can be modified by a `break` or `continue` statement (see below). In the case of `continue`,
the counter will be increased, as it is a new iteration.

## An addition independent to the DSGP 4 spec: `break` and `continue`

Under some circunstances, a user may want to modify the flow of a loop. That's where `break` and
`continue` are introduced. These extra additions were not expected by DSGP 4, but it's compatible.
This is the syntax:

```
!# No parenthesis are added (in that case, they're considered functions)

break;
continue;
```

These statements should be inside a "modifiable" loop. For example, if they are in the main level
(within no loops), it's a syntax error. Also, some loops cannot be modified like that, so they
should be inside a modifiable loop to accept `break` and `continue`.

These statements have the following usage:

- `break` will abort the first modifiable loop
- `continue` will go to the top of the first modifiable loop, as a new iteration [^1].

Here are some examples:

```
!# Good

while (True) {
    if (something) {
        !# this is good, because this `if` is inside a `while`
        break;
    }
    else {
        !# same here, the `else` is inside a `while`
        continue;
    }
}

!# Also good

repeat (9) {
    if (something) {
        !# good, since `if` is inside `repeat`
        continue;
    }
}

!# Wrong!

if (something) {
    !# The `if/elseif/else` family is not modifiable
    continue;
}

break;  !# no nesting? It is wrong!
```

## FAQ

### Why this DSGP depends in [DSGP 4][2]?

We have to say this: **we depend on DSGP 4 to proceed with this DSGP** [^2]. And that's because we depend
on the syntax defined by that DSGP. So, this DSGP is blocked by DSGP 4, and depends on it to exist.

In the case DSGP 4 gets rejected, this DSGP will have to be rejected too. If so, maybe another DSGP
will have to get adapted to the current DiddiScript behavior to achieve the same goal.

## What changes should the main parser ([DiddiParser 2][1]) receive?

If this DSGP gets accepted, it will be after DSGP 4 (see why above). So the parser will be ready for accepting most of
the statements proposed here. In those cases, only small additions will be needed (no major changes).

However, in the case of `break` and `continue`, that are independent to DSGP 4, the main parser's operations should
be modified. But nothing strong would be needed.

[^1]: For example, if the loop has a counter or something, it will be increased. Again, it is not repeating the iteration
      where `continue` was called, but goes to the next iteration.
[^2]: The only exception to this dependency is the `break` and `continue` statements, that are totally unexpected by DSGP 4.

[1]: https://github.com/DiddiLeija/diddiparser2
[2]: https://github.com/DiddiLeija/diddiparser2/blob/main/dsgp/dsgp-004.md
