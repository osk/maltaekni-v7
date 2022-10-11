def ld_recusive(a, b):
    """
    Calculate levenshtein distance between two strings via rescursion
    """
    # we only allow strings
    if not isinstance(a, str) or not isinstance(b, str):
        return 0

    # |a| = 0 => |b|
    if len(a) == 0:
        return len(b)

    # |b| = 0 => |a|
    if len(b) == 0:
        return len(a)

    if a[0] == b[0]:
        return ld_recusive(a[1:], b[1:])

    return 1 + min(
        [
            ld_recusive(a[1:], b),
            ld_recusive(a, b[1:]),
            ld_recusive(a[1:], b[1:]),
        ]
    )


def ld_wf(s, t):
    """
    Calculate levenshtein distance between two strings via Wagner–Fischer
    https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm
    """
    if not isinstance(s, str) or not isinstance(t, str):
        return 0

    m = len(s) + 1
    n = len(t) + 1
    d = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(1, m):
        d[i][0] = i

    for j in range(1, n):
        d[0][j] = j

    for j in range(1, n):
        for i in range(1, m):
            substitutionCost = 0 if s[i - 1] == t[j - 1] else 1

            d[i][j] = min(
                [d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + substitutionCost]
            )

    return d[m - 1][n - 1]
