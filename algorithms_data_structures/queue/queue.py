class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None

    def enqueue(self, value):
        node = Node(value)
        if self.front is None:
            self.front = node
        else:
            current = self.front
            while current.next is not None:
                current = current.next
            current.next = node

    def dequeue(self):
        if self.front is None:
            raise IndexError("Queue is empty")
        value = self.front.value
        self.front = self.front.next
        return value

    def is_empty(self):
        return self.front is None

    def size(self):
        count = 0
        current = self.front
        while current is not None:
            count += 1
            current = current.next
        return count

    def peek(self):
        if self.front is None:
            raise IndexError("Queue is empty")
        return self.front.value

    def __str__(self):
        values = []
        current = self.front
        while current is not None:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values)
