"""
Common tools for parser implementations,
including the DSGP 4 specs and low-level
operations.
"""


def findpos(item, tuplist, tuplist2=None):
    "Find a position in a statements list (or two lists, if provided)."
    for p in tuplist:
        if item in p:
            return True
    if tuplist2 is not None:
        for p in tuplist2:
            if item in p:
                return True
    return False


def treat_script(script):
    "Remove all the unnecesary lines (blank lines, comments)."
    sc2 = list()
    for line in script:
        line = line.split("!#")[0].rstrip()
        if len(line) < 1:
            continue
        sc2.append(line)
    return sc2


def get_stmts(script):
    """
    Find all the relevant statement positions,
    both the starts ('{') and the ends ('}').
    """
    ls, le = list(), list()
    cnt = -1
    cnt2 = -1
    for line in script:
        cnt2 += 1
        line = line.split("!#")[0].rstrip()
        if len(line) < 1:
            continue
        cnt += 1
        if "{" in line:
            ls.append((cnt, cnt2))
        if "}" in line:
            le.append((cnt, cnt2))
    return ls, le
