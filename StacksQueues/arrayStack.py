from queue import Empty


class ArrayStack:
    """LIFO (last in first out) implementation using a python list as underlying storage."""

    def __init__(self) -> None:
        """Create an empty stack."""
        self._data = []                         # non public list instance

    def __len__(self):
        """Return number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if stack is empty else False."""
        return len(self._data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)                    # new item stored at the end of the Arrays

    def top(self):
        """
        Return (but do not remove) the element at the top of the stack.
        
        Raise Empty exception if the stack is empty.
        """

        if self.is_empty():
            raise Empty('stack is empty')
        return self._data[-1]                   # last item in the list

    def pop(self):
        """
        Remove and return the element from the top of the stack.
        
        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('stack is empty')
        return self._data.pop()                # remove last item from the list