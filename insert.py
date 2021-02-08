class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_atbegin(head, data): # O(1)
    newnode = Node(data)
    if head is None:
        return newnode
    newnode.next = head
    head = newnode
    return newnode


def insert_atlast(head, data): # O(1)
    newnode = Node(data)
    temp = head
    if temp is None:
        return newnode
    while temp.next is not None:
        temp = temp.next
    temp.next = newnode
    newnode.next = None
    return head


def insert_atpos(head, pos, data): #O(min(pos, n))
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


def del_firstnode(head): #O(1)
    if head is None or head.next is None:
        return None
    curr = head
    while curr.next.next is not None:
        curr = curr.next
    curr.next = None
    return head


def del_lastnode(head): #O(n)
    if head is None or head.next is None:
        return Node
    temp = head
    while temp.next.next is not None:
        temp = temp.next
    temp.next = None
    return head

def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end = '->')
        temp = temp.next

head = None
head = insert_atbegin(head, 10)
head = insert_atbegin(head, 20)
head = insert_atbegin(head, 30)
head = insert_atbegin(head, 40)
head = insert_atbegin(head, 50)
#insert_atlast(head, 40)
#insert_atlast(head, 50)
#insert_atlast(head, 60)
#insert_atpos(head, 3, 15)
#insert_atpos(head, 4, 25)
printlist(head)
del_firstnode(head)
print()
printlist(head)
del_lastnode(head)
print()
printlist(head)

