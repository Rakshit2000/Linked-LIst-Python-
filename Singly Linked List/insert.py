class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_begin(head, data): # O(1)
    newnode = Node(data)
    if head is None:
        return newnode
    newnode.next = head
    head = newnode
    return newnode


def insert_at_last(head, data): # O(1)
    newnode = Node(data)
    temp = head
    if temp is None:
        return newnode
    while temp.next is not None:
        temp = temp.next
    temp.next = newnode
    newnode.next = None
    return head


def insert_at_pos(head, pos, data): #O(min(pos, n))
    newnode = Node(data)
    if pos == 1:
        newnode.next = head
        head = newnode
        return newnode
    curr = head
    for i in range(pos-2):
        curr = curr.next
        if curr == None:
            return head
    newnode.next = curr.next
    curr.next = newnode
    return head

def printlist(head):
    while head != None:
        print(head.data, end = '->')
        head = head.next

head = None
head = insert_at_begin(head, 10)
head = insert_at_begin(head, 20)
head = insert_at_begin(head, 30)
insert_at_last(head, 40)
insert_at_last(head, 50)
insert_at_last(head, 60)
insert_at_pos(head, 3, 15)
insert_at_pos(head, 4, 25)

printlist(head)

