"""
Common tools for parser implementations,
including the DSGP 4 specs and low-level
operations.
"""


def get_stmts(script):
    """
    Find all the relevant statement positions,
    both the starts ('{') and the ends ('}').
    """
    ls, le = list(), list()
    cnt = -1
    for line in script:
        line = line.split("!#")[0].rstrip()
        if len(line) < 1:
            continue
        cnt += 1
        if "{" in line:
            ls.append(cnt)
        if "}" in line:
            le.append(cnt)
    return ls, le
