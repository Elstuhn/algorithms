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
        
    return [hare, count] #returns [node, dist. from head]
