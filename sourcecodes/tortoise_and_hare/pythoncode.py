def tandh(head):
    tortoise = head
    hare = head
    while True:
        tortoise = tortoise.next_ #go to next node (update accordingly)
        hare = hare.next_.next_
        if tortoise == hare: #checks if both pointers are on the same node
            break
    hare = head
    count = 1
    while hare != tortoise:
        hare = hare.next_
        tortoise = tortoise.next_
        count += 1
        
    return [hare, count] #returns [node, dist. from head]
