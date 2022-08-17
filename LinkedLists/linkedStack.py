from curses.ascii import EM
from queue import Empty


class LinkedStack:
    """LIFO stack implementation using a singly linked list for storage."""


    """______________________nested _Node class______________________"""
    class _Node:
        """Lightweight, non public class for storing a singly linked list."""
        __slots__ = '_element', '_next'             # streamline memory usage

        def __init__(self, element, next) -> None:  # initialize node's fields
            self._element = element                 # reference to user's element
            self._next = next                       # reference to next node

    """______________________Stack methods______________________""" 
    def __init__(self) -> None:
        """Create an empty stack"""
        self._head = None                           # reference to the head node
        self._size = 0                              # number of stack elements

    def __len__(self):
        """Return the number of elements in the stack"""
        return self._size

    def is_empty(self):
        """Return True if stack is empty othereise False."""
        return self._size == 0
    
    def push(self, e):
        """Add element e to the top of the stack."""
        self._head = self._Node(e, self._head)      # create and link a new node
        self._size += 1
    
    def top(self):
        """Return (but do not remove) the element at the top of the stack
        
        Raise empty exception if the stack is emtpy.
        """
        if self.is_empty():
            raise Empty("stack is empty")
        return self._head._element                  # top of the stack is at the head of the list
    
    def pop(self):
        """Remove and return the element from the top of the stack (i.e LIFO).
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty("stack is empty")
        answer = self._head._element
        self._head = self._head._next               # bypass the former top node
        self._size -= 1
        return answer