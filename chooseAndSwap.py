"""
Pick any two chars in a string and swap all their appearances to get the lexicographically smallest
"""


def chooseAndSwap(s):

    for c in range(len(s)):
        c1 = c
        for c2 in range(c, len(s)):
            if s[c2] < s[c1]:
                c1 = c2
        if c1 != c:
            d = s[c1]
            d2 = s[c]
            break

    for e in range(len(s)):
        if s[e] == d:
            s = s[:e] + d2 + s[e + 1 :]
            continue

        if s[e] == d2:
            s = s[:e] + d + s[e + 1 :]
            print(s)

    return s


print("res = ", chooseAndSwap("actryhrds"))
