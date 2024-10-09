import unittest
from doubly_linked_list import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    
    def setUp(self):
        """This method runs before each test case."""
        self.dll = DoublyLinkedList()  # Initializing an empty DoublyLinkedList

    def test_append(self):
        self.dll.append(10)
        self.assertEqual(self.dll.head.data, 10)
        self.assertEqual(self.dll.head.next, None)  # Should be the only node

        self.dll.append(20)
        self.assertEqual(self.dll.head.next.data, 20)
        self.assertEqual(self.dll.head.next.prev.data, 10)  # Check the previous link

    def test_prepend(self):
        self.dll.append(20)
        self.dll.prepend(10)
        self.assertEqual(self.dll.head.data, 10)
        self.assertEqual(self.dll.head.next.data, 20)  # Should point to the next node

    def test_delete_node(self):
        self.dll.append(10)
        self.dll.append(20)
        node_to_delete = self.dll.search(10)
        self.dll.delete_node(node_to_delete)

        self.assertEqual(self.dll.head.data, 20)
        self.assertIsNone(self.dll.head.prev)  # Head should not have a previous node

    def test_search(self):
        self.dll.append(10)
        self.dll.append(20)
        found_node = self.dll.search(20)
        self.assertIsNotNone(found_node)
        self.assertEqual(found_node.data, 20)

        not_found_node = self.dll.search(30)
        self.assertIsNone(not_found_node)  # Node should not be found

if __name__ == "__main__":
    unittest.main()
