"""
0-1 knapshack. Items of weights and values, put them in a shack with limit weight W sush as they have maximum value. The item gets all or nothing (e.g. 0-1)
"""


def knapshack(weights, values, n, w, arr):

    if w <= 0 or sum(weights) < w or len(weights) <= n:
        return 0
    if weights[n] > w:
        return 0

    if arr[n][w] != -1:
        return arr[n][w]

    r1 = knapshack(weights, values, n + 1, w, arr)
    r2 = knapshack(weights, values, n + 1, w - weights[n], arr) + values[n]

    arr[n][w] = r1 if r1 > r2 else r2
    return r1 if r1 > r2 else r2


weights = [1, 4, 5, 6, 7]
values = [1, 5, 7, 9, 8]
w = 7

arr = list()
for i in range(len(weights) + 1):
    arr.append([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])


print("RES = ", knapshack(weights, values, 0, w, arr))
