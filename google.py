def jump(arr, oddOrEven, i):
    if i == len(arr) - 1:
        return True

    if oddOrEven == "odd":
        next = 1000
        nextIndex = -1
        for j in range(i, len(arr)):
            if arr[i] < arr[j] and arr[j] < next:
                next = arr[j]
                nextIndex = j

        if nextIndex == -1:
            return False

        return jump(arr, "even", nextIndex)

    if oddOrEven == "even":
        next = -1000
        nextIndex = -1
        for j in range(i, len(arr)):
            if arr[i] > arr[j] and arr[j] > next:
                next = arr[j]
                nextIndex = j

        if nextIndex == -1:
            return False

        return jump(arr, "odd", nextIndex)


dist = dict()

dist[1]["park"] = 0
print(dist)
