import math

"""
Given a sorted array arr[] of size N. Find the element that appears only once in the array. All other elements appear exactly twice
"""


def exactlyOnce(n):
    print(n)
    if len(n) == 0:
        return -1
    if len(n) == 1:
        return n[0]
    if len(n) == 2:
        return -1

    mid = math.floor(len(n) / 2)
    print("mid = ", mid)
    if n[mid] != n[mid - 1] and n[mid] != n[mid + 1]:
        return n[mid]

    r = exactlyOnce(n[0 : mid if n[mid] == n[mid + 1] else mid - 1])
    r2 = exactlyOnce(n[mid + 1 if n[mid] == n[mid - 1] else mid + 2 :])

    return r if r != -1 else r2


print("res = ", exactlyOnce([1, 1, 3, 3, 5, 5, 7, 7, 9, 9, 10, 10, 11]))
