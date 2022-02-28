# Changelog

## 1.2.0

**Syntax / breaking changes**

- When created, variables can store the value of other existing variables.

**Libraries**

- Modified and added stuff to the `simpleio` library:
  - Added `warning()`, to show warning messages.
  - Added `wait()`, to stop the execution for a lapse of time.
  - Enabled multiple arguments at `print_line()` and `print_text()`.
- Warn about the `sqlite` unstable status

**New features**

- The DiddiScript Python types (`diddiparser2.diddiscript_types`) have improved type conversors (`int()`, `float()`)
- The DiddiScript editor now has the option to set and load themes for colorizing the editor's interface. Added a "New file" option.

**Bug fixes**

- Sometimes, the parser ignored legitimate errors from DiddiScript functions, and stored a `Null` as the last value. Now it fails on legitimate errors.
- Fixed small issues with the editor. For example, removed the addition of newlines when saving. 

**Documentation**

We heavily reworked the docs.

- Replaced most of the `:ref:` references with `:doc:` references
- Refined the library docs
- Add an appendix session for less-relevant topics.

**Other changes**

- Updated dependencies

## 1.1.0.post1

This is a post release that fixes a mistake with `build`, that broke version 1.1.0. See
https://github.com/DiddiLeija/diddiparser2/issues/74 for more information.

## 1.1.0

**Syntax / breaking changes**

- The "tool functions" have been replaced by a `_builtin` module (see the "Libraries" section)
- Added "special variables", that cannot be overwritten by users:
  - `_memory` (which replaces `store_last_value` and stores the last obtained value)
  - `_endl` (which represents the newline)

**Libraries**

- New `_builtin` module, which is loaded by default and contains commonly used functions
- Improved the `fileio` library
- Improved and fixed the `math` library
- We simplified the `simpleio` library. Also, we added or modified:
  - `print_line()` (to print with a newline at the end)
  - `print_text()` (it now prints without newline)
- We removed the `subprocessing.run_python_code` function. We improved the `subprocessing.run_command` function, and added `subprocessing.run_python_cmd` (which calls the Python executable)

**DSGPs**

- DSGP 3: The ultimate extensions guide. This replaces any previous tutorial / guide of writing and using DiddiScript extensions.

**New features**

- `diddiparser2 -V` is now a shortcut for `diddiparser2 --version`
- Added attributes to the Python DiddiScript types (at `diddiparser2.diddiscript_types`)
- Added features (like a verbosity setting) to the DiddiScript editor GUI
- Added and controlled tests

**Bug fixes**

- Fixed issues with the parser's internal operations. For example, the value/variable resolutions.

**Other changes**

- Fixed the documentation issues left in 1.0.0
- We now use `build` for packaging
- We made a few changes to the parser's internal operations.
- Refined the docs
- Updated some dependencies

## 1.0.0

Initial release. It includes:

- The DiddiParser 2 CLI
- The DiddiScript REPL
- The DiddiScript editor
- A basic library
