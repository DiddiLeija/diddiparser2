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

If one of those steps fail, it is considered a syntax error (excluding the case where a function raises an error).

[^1]: When we talk about a "release", we're actually talking about the releases of [DiddiParser 2](https://github.com/DiddiLeija/diddiparser2),
      which is currently the official DiddiScript parser.
