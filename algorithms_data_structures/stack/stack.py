class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    
class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            raise IndexError("Stack is empty")
        value = self.top.value
        self.top = self.top.next
        return value

    def is_empty(self):
        return self.top is None

    def size(self):
        count = 0
        current = self.top
        while current is not None:
            count += 1
            current = current.next
        return count

    def peek(self):
        if self.top is None:
            raise IndexError("Stack is empty")
        return self.top.value

    def __str__(self):
        values = []
        current = self.top
        while current is not None:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(reversed(values))