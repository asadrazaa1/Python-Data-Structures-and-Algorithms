


class SequenceIterator:
    """An iterator for any of Python sequence types."""

    def __init__(self, sequence) -> None:
        """Create an iterator for the given sequence"""
        self._seq = sequence    # keep a reference to the underlying data
        self._k = -1            # will increment to 0 on the first call to next

    def __next__(self):
        """Return the next element, or else raise the StopIteration exception"""
        self._k += 1            # advance to next
        if self._k < len(self._seq):
            return self._seq[self._k] # return the data element
        raise StopIteration()         # there is no more date
    
    def __iter__(self):
        """By convention, an iterator must return itself as an iterator"""
        return self
