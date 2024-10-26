import unittest
from stack import Stack

class TestStack(unittest.TestCase):
    def test_push(self):
        s = Stack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.size(), 2)
        self.assertEqual(s.peek(), 2)

    def test_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.size(), 1)
        self.assertEqual(s.peek(), 1)

    def test_is_empty(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.push(1)
        self.assertFalse(s.is_empty())

    def test_size(self):
        s = Stack()
        self.assertEqual(s.size(), 0)
        s.push(1)
        s.push(2)
        self.assertEqual(s.size(), 2)

    def test_peek(self):
        s = Stack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.peek(), 2)

    def test_empty_stack(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.pop()

if __name__ == '__main__':
    unittest.main()