import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    
    def setUp(self):
        """This method runs before each test case."""
        self.ll = LinkedList(10)  # Initializing LinkedList with a single node (value = 10)
    
    def test_append(self):
        self.ll.append(20)
        self.assertEqual(self.ll.tail.value, 20)
        self.assertEqual(self.ll.length, 2)

    def test_prepend(self):
        self.ll.prepend(5)
        self.assertEqual(self.ll.head.value, 5)
        self.assertEqual(self.ll.length, 2)

    def test_pop(self):
        self.ll.append(15)
        popped_value = self.ll.pop()
        self.assertEqual(popped_value, 15)
        self.assertEqual(self.ll.tail.value, 10)
        self.assertEqual(self.ll.length, 1)

    def test_pop_first(self):
        self.ll.append(20)
        first_value = self.ll.pop_first()
        self.assertEqual(first_value, 10)
        self.assertEqual(self.ll.head.value, 20)
        self.assertEqual(self.ll.length, 1)

    def test_get(self):
        self.ll.append(15)
        node = self.ll.get(1)
        self.assertEqual(node.value, 15)

    def test_set(self):
        self.ll.append(15)
        result = self.ll.set(1, 25)
        self.assertTrue(result)
        self.assertEqual(self.ll.get(1).value, 25)

    def test_insert(self):
        self.ll.append(15)
        self.ll.insert(1, 12)
        self.assertEqual(self.ll.get(1).value, 12)
        self.assertEqual(self.ll.length, 3)

    def test_remove(self):
        self.ll.append(15)
        removed_node = self.ll.remove(1)
        self.assertEqual(removed_node, 15)
        self.assertEqual(self.ll.length, 1)

    def test_reverse(self):
        self.ll.append(20)
        self.ll.append(30)
        self.ll.reverse()
        self.assertEqual(self.ll.head.value, 30)
        self.assertEqual(self.ll.tail.value, 10)

    def test_print_list(self):
        self.ll.append(15)
        self.ll.append(20)
        self.assertEqual(self.ll.head.value, 10)
        self.assertEqual(self.ll.tail.value, 20)
        self.assertEqual(self.ll.length, 3)

if __name__ == "__main__":
    unittest.main()