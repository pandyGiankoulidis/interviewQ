"""
Given array find all triplets that add to a given number
"""

"""
1.Two pointer solution
"""


def threeSumTwoPointer(arr, n):
    arr.sort()
    res = list()

    for i in range(len(arr)):
        pointerLeft = i + 1
        pointerRight = len(arr) - 1
        while pointerLeft < pointerRight:
            if arr[pointerLeft] + arr[pointerRight] + arr[i] == n:
                res.append([arr[i], arr[pointerLeft], arr[pointerRight]])
                pointerLeft = pointerLeft + 1
                pointerRight = pointerRight - 1
            if arr[pointerLeft] + arr[pointerRight] + arr[i] < n:
                pointerLeft = pointerLeft + 1
            if arr[pointerLeft] + arr[pointerRight] + arr[i] > n:
                pointerRight = pointerRight - 1

    return res


"""
2.Hash solution
"""


def threesumHash(arr, n):
    res = list()
    for i in range(len(arr)):
        s = list()
        partialSum = n - arr[i]
        for j in range(i, len(arr)):
            requiredValue = partialSum - arr[j]
            if requiredValue in s:
                res.append([arr[i], arr[j], requiredValue])
            s.append(arr[j])

    return res


"""
PLAYGROUND
"""
r = [3, 5, -2, -1, 4, 2, 11, -6, -3]
t = 4

print("Res = ", threeSumTwoPointer(r, t))
print("ResHash = ", threesumHash(r, t))
