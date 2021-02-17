class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def sorted_linkedlist(head, x): #O(n)
    newnode = Node(x)

    if head == None:
        return newnode
    elif x < head.data:
        newnode.next = head
        return newnode
    else:
        curr = head

        while curr.next != None and curr.next.data < x:
            curr = curr.next

        newnode.next = curr.next
        curr.next = newnode
        return head


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

h = head
while h != None:
    print(h.data, end = '->')
    h = h.next

print()

h = sorted_linkedlist(head, 25)

h = head
while h != None:
    print(h.data, end = '->')
    h = h.next








