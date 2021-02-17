class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""
O(Linear time)

def insert_at_begin(head, x): 
    newnode = Node(x)
    if head is None:
        newnode.next = newnode
        return newnode
    temp = head
    while temp.next is not head:
        temp = temp.next

    temp.next = newnode
    newnode.next = head
    return newnode
"""


# O(Constant time)
def insert_at_begin(head,x):
    newnode = Node(x)
    if head is None:
        newnode.next = newnode
        return newnode

    newnode.next = head.next
    head.next = newnode
    head.data, newnode.data = newnode.data, head.data  # swapping data
    return head


def insert_at_last(head, x):
    newnode = Node(x)
    if head is None:
        newnode.next = newnode
        return newnode
    temp = head
    while temp.next is not head:
        temp = temp.next
    temp.next = newnode
    newnode.next = head
    return head


def print_list(head):
    if head is None:
        return
    print(head.data, end="->")
    temp = head.next
    while temp is not head:
        print(temp.data, end="->")
        temp = temp.next

    print()

head = Node(20)
head.next = Node(30)
head.next.next = head
print_list(head)

insert_at_begin(head, 10)

print_list(head)

insert_at_last(head, 40)
print_list(head)
insert_at_last(head, 50)
print_list(head)
