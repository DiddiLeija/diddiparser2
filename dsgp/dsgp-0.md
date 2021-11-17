# DSGP 0 -- DiddiScript Grammar Proposals scheme

| Author        | Author email         | Status   |
|---------------|----------------------|----------|
| Diego Ramirez | dr01191115@gmail.com | Approved |

## Overview

This proposal sketches the scheme for the **DiddiScript Grammar Proposals**
(or **DSGP**). All the DSGPs after this one should follow this scheme to be
accepted. It also provides an "expected proposal" and some rules that all of
the DSGPs should follow.

## What's expected from a DSGP

DiddiScript has a specific grammar, with specific rules. However, those
rules can be extended or modified by a DSGP. The idea of DSGPs is
proposing an important change to the Diddiscript grammar.

A DSGP _should not_ be focused in proposing new libraries. Those
changes should be covered in an issue at the parser's repository.
For example, in the [DiddiParser 2 GitHub Issues page][1]. 

It is recommended to add examples to a DSGP, to explain how does the
proposed grammar will affect the DiddiScript behavior. Also, if it takes
references, they have alink to the original source, or at least, a reference
to the source.

## Acceptance cycle of a DSGP

A DSGP should be proposed to the [GitHub repository where DSGPs are stored][2] as
a pull request. On the pull request, the main idea of the proposal will
be discussed, and the document may change. During that process, the status of the
DSGP may change (see the _DSGP statuses_ section below).

### DSGP statuses

These statuses tell if a DSGP has been accepted, is in development, or has been
rejected:

- **Draft:** The DSGP is not ready yet to be considered. It needs more information, standardisation
or any other required information.

- **Pending:** The decision (or the discussion behind accepting the DSGP) hasn't finished yet,
but the document is ready to be considered.

- **Approved:** The proposal has been accepted, and it has been applied (or will be applied in the
near future). The related pull requests can be merged into the main repository.

- **Rejected:** The DSGP can't be applied, or the general idea has been rejected. Any related pull
request is closed. New proposals to the same idea should belong to a new DSGP.

## Markup language of DSGPs

The markup language used for writing DSGPs is **GitHub Markdown**. All the
DSGPs should use this format to be accepted.

## DSGP template

This is a template of a DSGP. The author of future DSGPs can use this template to
write the document. Replace the `{...}` spaces with the required information:

```markdown
## DSGP {number of the DSGP} -- {title}

| Author        | Author email         | Status   |
|---------------|----------------------|----------|
| {author name} | {valid email}        | Draft    |

## Overview

{A short overview to your document}

## {All the sections of the DSGP}

...
```

A reference to an external source can be added with the following Markdown syntax:

```markdown
[This is a reference to a site][1]. A DSGP can make references to
any place in the Internet, like [this Google page][2].

<!---
The references are defined below, and can be used
multiple times.
--->

[1]: https://example.com
[2]: https://google.com
```

<!--- References --->

[1]: https://github.com/DiddiLeija/diddiparser2/issues
[2]: https://github.com/DiddiLeija/diddiparser2/tree/main/dsgp
