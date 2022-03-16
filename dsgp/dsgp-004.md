# DSGP 4 -- DiddiScript parser, version 2

| Author        | Author email         | Status   |
|---------------|----------------------|----------|
| Diego Ramirez | dr01191115@gmail.com | Draft    |

## Overview

The version 1 of the DiddiScript parser rules (applied in the 1.x releases [^1]) are useful on strict cases (where
no decisions are allowed). However, programming usually needs more flexible parsing. This DSGP proposes a new syntax to
parse the steps easier, to prepare the scenario for future features.

## Description of the old parser (version 1)

The old parser (used in the 1.x releases) works as follows:

- Remove the inline (`!#`) comments, and all the empty lines
- Check that the remaining lines end with a semicolon (`;`)
- Run the remaining lines:
  - Decide if a line is a variable definition or a function call
  - Execute the corresponding action

If one of those steps fail, it is considered a syntax error (excluding the case where a function raises an error, where it
is considered a "run failure").

### Pros and cons of the old parser

**Pros**

  - It's easier to maintain, because it's linear and predictable.
  - In simple examples and some use cases, there's no need to have decisions or loops.

**Cons**
  - In most of the cases, you may want to control the program flow, but this parser gives no chance for that.
  - It's rigid, so it becomes hard to provide new syntax
  - The ending semicolon is actually useless, because there's no chance to have multiple stuff in the same line [^2]

## Description of the new parser (version 2)

The new parser's intention is to make it easier to define new syntax, and being more flexible. The proposal of the "basic
flow" is the following:

- Remove the inline (`!#`) comments, and all the empty lines
- Statements [^3] are separated and nested where needed.
  - If there are unclosed statements, a syntax error will be raised.
- Split all the semicolons (`;`) to identify the steps. This will run on every place where steps are identified.
- Run the remaining lines, according to how does the step look like.

[^1]: When we talk about a "release", we're actually talking about the releases of [DiddiParser 2](https://github.com/DiddiLeija/diddiparser2),
      which is currently the official DiddiScript parser.
[^2]: In case this DSGP is dropped or something like that, there's a less-fancy alternative: remove the semicolon usage. However, it won't fix
      the current issue with the limited syntax.
[^3]: This DSGP will define the "statements syntax". However, it will be just a sketch, so other DSGPs can model recognized statements.
