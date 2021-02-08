"""
Time Complexity: O(n)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def search_linked_list(head, x):
    while head != None:
        if head.data == x:
            return 1
        head = head.next
    return -1

head = Node(10)
head.next = Node(20)
head.next.next = Node(20)
head.next.next.next = Node(20)
x = 20
print(search_linked_list(head, x))

