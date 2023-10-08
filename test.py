import unittest
from main import Queue


class TestQueue(unittest.TestCase):
    def test_queue_empty(self):
        q = Queue(5)
        self.assertRaises(Exception, q.dequeue)

    def test_queue_full(self):
        q = Queue(1)
        q.enqueue(1)
        self.assertRaises(Exception, q.enqueue, 2)

    def test_queue_enqueue_dequeue(self):
        q = Queue(5)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertRaises(Exception, q.dequeue)

