import unittest
from queue import Queue

class TestQueue(unittest.TestCase):
    def test_enqueue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.size(), 2)
        self.assertEqual(q.peek(), 1)

    def test_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.size(), 1)
        self.assertEqual(q.peek(), 2)

    def test_is_empty(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue(1)
        self.assertFalse(q.is_empty())

    def test_size(self):
        q = Queue()
        self.assertEqual(q.size(), 0)
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.size(), 2)

    def test_peek(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.peek(), 1)

    def test_empty_queue(self):
        q = Queue()
        with self.assertRaises(IndexError):
            q.dequeue()

if __name__ == '__main__':
    unittest.main()