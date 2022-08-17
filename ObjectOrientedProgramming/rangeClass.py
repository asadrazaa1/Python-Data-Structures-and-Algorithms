"""Creating an implemention of a class that mimics the python's built-in range class"""

class Range:
    """A class that mimics python's built-in range class"""

    def __init__(self, start, stop=None, step=1) -> None:
        """Initialize a Range instance

        Semantics is similar to the built-in range class
        """

        if step == 0:
            raise ValueError("step cannot be 0")

        if stop is None:            # special case of range(n)
            start, stop = 0, start  # should be treated as if range(m ,n)
        
        # calculate the effective length once
        self._length = max(0, (stop-start+step-1)//step)

        # need knowledge of the start and step(but not support) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        """Return the number of entries in the range."""
        return self._length

    def __getitem__(self, k):
        """Return entry at the index k(using standard interpretation if negative)"""

        if k < 0:
            k += len(self)          # attempt to convert negative index
        
        if not 0 <= k < self._length:
            raise IndexError("index out of range")

        return self._start + k * self._step