# Changelog

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
