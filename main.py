# enqueue
# dequeue
# length
# if above capacity, throw exception

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Queue:
    def __init__(self, length: int) -> None:
        self.length = length
        self.head = Node("dummy")
        self.tail = self.head
        self.size = 0

    def enqueue(self, val):
        if self.size >= self.length:
            raise Exception("Maximum length reached")

        self.size += 1

        temp = Node(val)
        self.tail.next = temp
        self.tail = temp

    def dequeue(self):
        if self.size <= 0:
            raise Exception("Queue is empty")

        self.size -= 1

        temp = self.head.next
        self.head.next = temp.next

        return temp.val
