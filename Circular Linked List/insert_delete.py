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


def insert_at_last(head, x): #O(n)
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


def delete_head(head): #O(1)
    if head is None:
        return None
    if head.next is head:
        return None
    head.data = head.next.data
    head.next = head.next.next
    return head

def delete_kth_node(head, k):
    if head is None:
        return head
    if k == 1:
        return delete_kth_node(head)
    temp = head
    for i in range(k-2):
        temp = temp.next
    temp.next = temp.next.next
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

delete_head(head)
print_list(head)

delete_kth_node(head,3)
print_list(head)
