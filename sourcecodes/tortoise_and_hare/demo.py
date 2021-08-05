def tandh(head):
    tortoise = head
    hare = head
    while True:
        tortoise = tortoise.next_
        hare = hare.next_.next_
        if tortoise == hare:
            break
    hare = head
    count = 1
    while hare != tortoise:
        hare = hare.next_
        tortoise = tortoise.next_
        count += 1
        
    print(count)
    print(f"Node: {hare}\nNode Value: {hare.value}")

class Node:
    def __init__(self, value):
        self.value = value
        self.next_ = None

class LinkedList:
    def __init__(self, head):
        self.head = head

current = Node(3)
LL = LinkedList(current)
for i in range(5):
    newnode = Node(i*2)
    current.next_ = newnode
    current = newnode
current.next_ = LL.head.next_.next_.next_

tandh(LL.head)
