# DSGP 5 -- First statements

| Author        | Author email         | Status   |
|---------------|----------------------|----------|
| Diego Ramirez | dr01191115@gmail.com | Draft    |

## Overview

In the 1.x series of [DiddiParser 2][1], having statements was just impossible, unless
you figured out a way using functions.

But after [DSGP 4][2] acceptance, there's a chance for a new piece of the DiddiScript syntax:
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

## FAQ

### Why this DSGP depends in [DSGP 4][2]?

We have to say this: **we depend on DSGP 4 to proceed with this DSGP**. And that's because we depend
on the syntax defined by that DSGP. So, this DSGP is blocked by DSGP 4, and depends on it to exist.

In the case DSGP 4 gets rejected, this DSGP will have to be rejected too. If so, maybe another DSGP
will have to get adapted to the current DiddiScript behavior to achieve the same goal.

[1]: https://github.com/DiddiLeija/diddiparser2
[2]: https://github.com/DiddiLeija/diddiparser2/blob/main/dsgp/dsgp-004.md
