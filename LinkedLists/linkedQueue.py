from curses.ascii import EM
from hashlib import new
from queue import Empty


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""


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
        self._head = None                           # reference to the head node
        self._tail = None
        self._size = 0                              # number of queue elements

    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size

    def is_empty(self):
        """Return True if queue is empty othereise False."""
        return self._size == 0
    
    def enqueue(self, e):
        """Add element e to the back of the queue."""
        newest = self._Node(e, None)      # node will be new tail node
        if self.is_empty():
            self._head = newest           # special case: previously empty
        else:
            self._tail._next = newest   
        self._tail = newest               # update reference to the tail node
        self._size += 1
    
    def first(self):
        """Return (but do not remove) the element at the front of the queue
        
        Raise empty exception if the queue is emtpy.
        """
        if self.is_empty():
            raise Empty("queue is empty")
        return self._head._element                  # top of the queue is at the head of the list
    
    def dequeue(self):
        """Remove and return the first element from the queue (i.e FIFO).
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("queue is empty")
        answer = self._head._element
        self._head = self._head._next              
        self._size -= 1
        if self.is_empty():                         # special case , queue is emtpy
            self._tail = None                       # removed head had been the tail
        return answer