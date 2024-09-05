import copy


def bfs(islands, queue):
    if len(queue) == 0:
        return

    next = queue.pop()
    i = next[0]
    j = next[1]

    islands[i][j] = 0

    if i > 0 and islands[i - 1][j] == 1:
        queue.add((i - 1, j))

    if i < len(islands) - 1 and islands[i + 1][j] == 1:
        queue.add((i + 1, j))

    if j > 0 and islands[i][j - 1] == 1:
        queue.add((i, j - 1))

    if j < len(islands) - 1 and islands[i][j + 1] == 1:
        queue.add((i, j + 1))

    bfs(islands, queue)


arr = [
    [0, 1, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 1],
]

islands = copy.deepcopy(arr)

for j in range(len(arr)):
    q = set()
    if arr[0][j] == 1:
        q.add((0, j))
        bfs(islands, q)

    if arr[len(arr) - 1][j] == 1:
        q.add((len(arr) - 1, j))
        bfs(islands, q)


"""for i in range(len(arr)):
    for j in range(len(arr) - 1):
        if islands[i][j] == 1:
            arr[i][j] == 0"""

print(arr)
