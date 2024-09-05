"""
Longest common subsequence

e.g. ABCD and BDAE have 2 (BD)
"""


def LCS(s1, s2, arr):
    if len(s1) == 0 or len(s2) == 0:
        return 0

    i1 = len(arr) - len(s1)
    i2 = len(arr) - len(s2)
    if arr[i1][i2] != -1:
        return arr[i1][i2]

    r1 = 0
    for c in range(len(s2)):
        if s2[c] == s1[0]:
            r1 = 1 + LCS(s1[1:], s2[c:], arr)
            break

    r2 = LCS(s1[1:], s2, arr)

    arr[i1][i2] = r1 if r1 > r2 else r2
    return r1 if r1 > r2 else r2


print(
    "res = ",
    LCS(
        "ABCDGHR",
        "AEFHR",
        list(
            [
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
            ]
        ),
    ),
)
