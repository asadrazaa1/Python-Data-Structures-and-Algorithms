from curses.ascii import EM
from hashlib import new
from queue import Empty
import re


class CircularQueue:
    """Queue implementation using a singly linked list for storage."""


    """______________________nested _Node class______________________"""
    class _Node:
        """Lightweight, non public class for storing a singly linked list."""
        __slots__ = '_element', '_next'             # streamline memory usage

        def __init__(self, element, next) -> None:  # initialize node's fields
            self._element = element                 # reference to user's element
            self._next = next                       # reference to next node

    """______________________Queue methods______________________""" 
    def __init__(self) -> None:
        """Create an empty queue"""
        self._tail = None
        self._size = 0                              # number of queue elements

    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size

    def is_empty(self):
        """Return True if queue is empty othereise False."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue
        
        Raise empty exception if the queue is emtpy.
        """
        if self.is_empty():
            raise Empty("queue is empty")
        head = self._tail._next
        return head._element
    
    def enqueue(self, e):
        """Add element e to the back of the queue."""
        newest = self._Node(e, None)            # node will be the new tail node
        if self.is_empty():
            newest._next = newest               # starting circularly
        else:
            newest._next = self._tail._next     # new node points to the head
            self._tail._next = newest           # old tail points to the new node
        self._tail._next = newest               # new node becomes the tail
        self._size += 1

    def dequeue(self):
        """Remove and return the first element from the queue.
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("queue is emtpy")
        oldhead = self._tail._next             
        if self._size == 1:                     # removing only element
            self._tail = None                   # queue becomes empty
        else:
            self._tail._next = oldhead._next    # bypass the old head
        self._size -= 1
        return oldhead._element
    
    def rotate(self):
        """Rotate front element to the back of the queue"""
        if self._size > 0:
            self._tail = self._tail._next       # old head becomes new tail

