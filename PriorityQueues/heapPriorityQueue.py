from pyparsing import Empty

from priorityQueueBase import PriorityQueueBase


class HeapPriorityQueue(PriorityQueueBase):  # base  class define _Item
    """A min oriented priority queu implemented with a binary heap"""

    # ------------------ nonpublic behaviours ------------------
    def _parent(self, j):
        return (j-1)/2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)  # index beyond end of limit

    def _has_right(self, j):
        return self._right(j) < len(self._data)  # index beyond end of limit

    def _swap(self, i, j):
        """Swap the elements at indices i and j of Arrays"""
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)        # Recursion

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left          # right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)         # Recursion

    # ------------------ public behaviours ------------------
    def __init__(self):
        """Create a new empty priority queue"""
        self._data = []

    def __len__(self):
        """Return  the number of items in the priority queue"""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair to the priority queue"""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)       # up heap newly added position

    def min(self):
        """Return but do not remove k,v with minimum key

        Raise Empty exception if empty
        """
        if self.is_empty():
            raise Empty('priority queue is empty')
        item = self._data[0]
        return item._key, item._value

    def remove_min(self):
        """Remove and return k,v with minimum key

        Raise Empty exception if empty
        """
        if self.is_empty():
            raise Empty("priority queue is empty")
        self._swap(0, len(self._data) - 1)          # put minimum item at the end
        item = self._data.pop()                     # and remove it from the list
        self._downheap(0)
        return item._key, item._value
