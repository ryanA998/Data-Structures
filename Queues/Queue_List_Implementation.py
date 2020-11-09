#Queue Single List Implementation
#Author: Ryan Arendt
#Implementation adapted from:
#https://runestone.academy/runestone/books/published/pythonds3/BasicDS/ImplementingaQueueinPython.html

#Unlike the CS: 331 lecture we dont care each Queue operation is O(1)
class Queue: 

    def __init__(self):
        self._items = [] 

    def is_empty(self):
        return not bool(self._items)

    def enqueue(self, item): 
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)
