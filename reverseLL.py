class Node:
    def __init__(self, value):
        self.value = value

    def setNext(self, next):
        self.next = next


def reverseLinkedList(head):

    prev = None
    curr = head
    next = None

    while curr is not None:
        next = curr.next if hasattr(curr, "next") else None
        curr.next = prev
        prev = curr
        curr = next


n1 = Node(4)
n2 = Node(7)
n3 = Node(12)
n4 = Node(1)
n5 = Node(2)
n6 = Node(9)

n1.setNext(n2)
n2.setNext(n3)
n3.setNext(n4)
n4.setNext(n5)
n5.setNext(n6)

head = n1
while head is not None:
    print("--> ", head.value)
    head = head.next if hasattr(head, "next") else None

reverseLinkedList(n1)

head = n6
while head is not None:
    print("--> ", head.value)
    head = head.next if hasattr(head, "next") else None
