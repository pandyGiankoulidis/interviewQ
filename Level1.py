from math import inf
import random
import Node
import btNode
import MyQueue
import math

"""
AUXILIARY FUNCTIONS
"""


def createGraph(size):
    graph = []
    for i in range(size):
        n = Node.Node(random.randint(0, size - 1), i)

        for j in range(random.randint(0, size - 1)):
            n.setAdjacentNode(random.randint(0, size - 1))

        graph.append(n)

    return graph


def printGraph(g):
    for n in g:
        print(
            "Node #",
            n.index,
            " with value = ",
            n.value,
            " and connections to:",
            n.adjacencyList,
        )


def createBinaryTree(parent, depth):
    if depth == 0:
        return
    nL = btNode.binaryTreeNode(random.randint(0, 100))
    nR = btNode.binaryTreeNode(random.randint(0, 100))
    createBinaryTree(nL, depth - 1)
    createBinaryTree(nR, depth - 1)
    parent.setLeftChild(nL)
    parent.setRightChild(nR)


def printBTreePreOrder(tree):

    print("VISIT Node = ", tree.value)
    if hasattr(tree, "left"):
        printBTreePreOrder(tree.left)

    if hasattr(tree, "right"):
        printBTreePreOrder(tree.right)


def printBTreeInOrder(tree):
    if hasattr(tree, "left"):
        printBTreeInOrder(tree.left)

    print("VISIT Node = ", tree.value)
    if hasattr(tree, "right"):
        printBTreeInOrder(tree.right)


def depthFirstSearch(n, graph):
    graph[n].hasBeenVisited = True
    for nn in graph[n].adjacencyList:
        if graph[nn].hasBeenVisited == False:
            depthFirstSearch(nn, graph)


"""
1. Decide if there's a root between two nodes
"""
"""def thereIsConnection(a, b, graph):
    depthFirstSearch(a, graph)
    if graph[b].hasBeenVisited:
        print("There is route from ",a," to ",b)
        return
    
    for n in range(len(graph)):
        nd = graph[n]
        nd.hasBeenVisited = False
        graph[n] = nd 

    depthFirstSearch(b, graph)
    if graph[a].hasBeenVisited:
        print("There is route from ",b," to ",b)
        return
    
    print("There is no route between ",a," and ",b)



g = createGraph(10)
thereIsConnection(0,8,g)
"""

"""
2. Convert a binary tree to linked list
"""
"""def breadthFStoLL(tree):
    
    queue = []
    queue.append(tree)
    linkedList = []

    while queue:
        tree = queue.pop(0)
        linkedList.append(Node.Node(tree.value, 0))
        if hasattr(tree, 'left'):
            queue.append(tree.left)

        if hasattr(tree, 'right'):
            queue.append(tree.right)

    return linkedList


root = btNode.binaryTreeNode(random.randint(0, 100))
createBinaryTree(root, 3)

ll = breadthFStoLL(root)

printBTreePreOrder(root)

for l in ll:
    print("N = ",l.value)
"""

"""
3. Implement queue with two stacks 
"""
"""q = MyQueue.MyQueue("queue")

q.push(32)
q.push(43)
q.push(11)
q.pop()
q.push(19)
q.pop()
q.push(88)
q.pop()

for i in q.stackDequeue:
    print(i)
    """

"""
4. Unique characters in string
"""
"""text = "3412uhj1"

for i in range(256):
    c = chr(i)
    occurs = 0
    for a in text:
        if a == c:
            occurs = occurs + 1
            if occurs > 1:
                print("False")
                break
"""


"""
5. Permutation string of the other
"""


def perm(s1, s2):
    if len(s1) != len(s2):
        return False

    s1Chars = dict()
    for c in s1:
        if c not in s1Chars:
            s1Chars[c] = 1
        else:
            s1Chars[c] = s1Chars[c] + 1

    for c in s2:
        if c not in s1Chars:
            return False

        s1Chars[c] = s1Chars[c] - 1

    for k, v in s1Chars.items():
        print(v)
        if v != 0:
            return False


"""f = perm("34rtRR", "r4R3tR")
print("It is ", f)
"""

"""
6. mxn set to 0
"""


"""def setToZero(mat):
    zeros = list()
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 0:
                zeros.append((i, j))

    print(zeros)
    """


"""
7. Rotate matrix
"""


"""def rotateMatrix(N):
    nm = N
    for i in range(len(N), 0, -1):
        for j in range(len(N)):
            nm[j][len(N) - i] = N[i - 1][j]

    return nm


g = [[3, 4, 1, 2], [12, 44, 89, 33], [77, 41, 8, 16], [42, 84, 87, 0]]

print("res = ", rotateMatrix(g))
"""


def finder(A, x):
    if len(A) == 0:
        return -1
    if x < A[0]:
        return -1
    if len(A) == 1:
        return A[0]
    mid = math.floor(len(A) / 2)
    if A[mid] == x:
        return x

    return finder(A[0:mid], x) if A[mid] > x else finder(A[mid:], x)


print("Found ", finder([], 21))
