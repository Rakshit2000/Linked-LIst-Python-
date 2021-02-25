class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def insert_begin(head, x): #(O(1))
    newnode = Node(x)
    if head is not None:
        head.prev = newnode
    newnode.next = head
    return newnode


def insert_end(head, x):
    newnode = Node(x)
    if head is None:
        return None
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = newnode
    newnode.prev = temp
    return head


def del_head(head):  #(O(1))
    if head is None or head.next is None:
        return None
    head = head.next
    head.prev = None
    return head


def del_tail(head): # O(n)
    if head is None or head.next is None:
        return None
    temp = head
    while temp.next.next is not None:
        temp = temp.next
    temp.next = None
    return head


def reverse(head):
    if head is None:
        return None
    if head.next is None:
        return head
    curr = head
    prev = None
    while curr is not None:
        prev = curr
        curr.next, curr.prev = curr.prev, curr.next
        curr = curr.prev
    return prev


def print_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end='->')
        temp = temp.next
    print()


head = None
head = insert_begin(head, 10)
head = insert_begin(head, 20)
head = insert_begin(head, 30)
head = insert_begin(head, 40)
print_list(head)

head = insert_end(head,50)
print_list(head)

'''
head = del_head(head)
print_list(head)

head = del_tail(head)
print_list(head)
'''

head = reverse(head)
print_list(head)