import ctypes

class DynamicArray:
    """A dynamic Arrays class akin to a simplified python list"""

    def __init__(self) -> None:
        """Create an empty Arrays"""
        self._n=0                                   # count actual elements 
        self._capacity=1                            # default Arrays capacity
        self._A=self._make_array(self._capacity)    # low-level Arrays

    def __len__(self):
        """Return number of elements stored in the Arrays"""
        return self._n
    
    def __getitem__(self, k):
        """Return the element at index k"""
        if not 0 <= k < self._n:
            return IndexError('invalid index')
        return self._A[k]                           # return the element

    def append(self, obj):
        """Add object to the end of the Arrays"""
        if self._n == self._capacity:               # not enough room
            self._resize(2*self._capacity)          # double capacity
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):                           # non public utility
        """Resize internal arrary to capacity c"""
        B = self._make_array(c)                     # new Arrays
        for k in range(self._n):                    # for each existing value
            B[k] = self._A[k]
        self._A = B                                 # using the bigger Arrays
        self._capacity = c

    def _make_array(self, c):                       # non public utility
        """Return new Arrays with capacity c"""
        return (c * ctypes.py_object)