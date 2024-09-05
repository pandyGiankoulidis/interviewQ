class Node:
    def __init__(self, v, i):
        self.value = v
        self.index = i
        self.adjacencyList = []
        self.hasBeenVisited = False

    def setAdjacentNode(self, index):
        if index in self.adjacencyList or index == self.index:
            return
        self.adjacencyList.append(index)

    