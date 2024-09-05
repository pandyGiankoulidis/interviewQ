Blocks = [
    {"store": False, "gym": True, "school": False},
    {"store": False, "gym": False, "school": False},
    {"store": True, "gym": False, "school": False},
    {"store": False, "gym": True, "school": True},
    {"store": False, "gym": True, "school": False},
]

Reqs = ["store", "gym", "school"]


blockDist = dict()
for block in range(len(Blocks)):
    blockDist[block] = dict()
    for req in Reqs:
        if Blocks[block][req]:
            blockDist[block][req] = 0
        else:
            if block > 0:
                blockDist[block][req] = (
                    blockDist[block - 1][req] + 1
                    if blockDist[block - 1][req] != -1
                    else -1
                )
            else:
                blockDist[block][req] = -1


for block in range(len(Blocks) - 2, -1, -1):
    for req in Reqs:
        if not Blocks[block][req]:
            prevDist = blockDist[block + 1][req] + 1
            if blockDist[block][req] == -1:
                blockDist[block][req] = prevDist
                continue
            if prevDist < blockDist[block][req]:
                blockDist[block][req] = prevDist

print(blockDist)
