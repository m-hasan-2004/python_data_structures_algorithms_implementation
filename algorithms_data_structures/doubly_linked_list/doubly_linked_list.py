class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list

    def append(self, data):
        """Add a node to the end of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        last = self.head
        while last.next:  # Traverse to the last node
            last = last.next
        last.next = new_node  # Link the new node
        new_node.prev = last  # Set the previous pointer

    def prepend(self, data):
        """Add a node to the beginning of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        new_node.next = self.head  # Link new node to the current head
        self.head.prev = new_node  # Set the previous pointer of current head
        self.head = new_node  # Update head to the new node

    def delete_node(self, node):
        """Delete a node from the list."""
        if not self.head or not node:
            return
        if self.head == node:  # If the node to be deleted is the head
            self.head = node.next
        if node.next:  # Change the next only if the node to be deleted is NOT the last node
            node.next.prev = node.prev
        if node.prev:  # Change the prev only if the node to be deleted is NOT the first node
            node.prev.next = node.next

        node = None  # Free the memory

    def display_forward(self):
        """Display the list from head to end."""
        current = self.head
        while current:
            print(current.data, end=' <-> ')
            current = current.next
        print("None")

    def display_backward(self):
        """Display the list from end to head."""
        current = self.head
        if not current:  # If the list is empty
            print("None")
            return
        while current.next:  # Traverse to the last node
            current = current.next
        while current:  # Traverse backward from the last node
            print(current.data, end=' <-> ')
            current = current.prev
        print("None")

    def search(self, key):
        """Search for a node with a specific value."""
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next
        return None  # Return None if the key is not found

# Example usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.prepend(5)
    
    print("List after appending and prepending:")
    dll.display_forward()  # Display forward
    
    node_to_delete = dll.search(20)
    if node_to_delete:
        dll.delete_node(node_to_delete)
    
    print("List after deleting 20:")
    dll.display_forward()  # Display forward
    
    print("List displayed backward:")
    dll.display_backward()  # Display backward