from random import randrange

from mapBase import MapBase


class HashMapBase(MapBase):
    """"Abstract base class for map using hash-table with MAD cmpression"""

    def __init__(self, cap=11, p=1093451221):
        """Create an empty hashtable map"""
        self._table = cap * [None]
        self._n = 0                             # number of entries in the map
        self._prime = p                         # prime for MAD compression
        self._scale = 1 + randrange(p-1)        # scale from 1 to p-1 for MAD
        self._shift = randrange(p)              # scale from 0 to p-1 for MAD

    def _hash_function(self, k):
        return (hash(k)*self._scale + self._shift) % self._prime % len((self._table))

    def __len__(self):
        return self._n

    def __getitem__(self, item):
        j = self._hash_function(item)
        return self._bucken_getitem(j, item)    # may raise key error

    def __setitem__(self, key, value):
        j = self._hash_function(value)
        self._bucket_setitem(j, key, value)     # subroutine maintains self._n
        if self._n > len(self._table) // 2:     # keep load factor <= 0.5
            self._resize(2 * len(self._table) - 1)   # number 2^x-1 os often prime

    def __delitem__(self, key):
        j = self._hash_function(key)
        self._bucket_delitem(j, key)            # may raise key error
        self._n -= 1

    def _resize(self, c):
        """Resize bucked Arrays to capacity c"""
        old = list(self.items())            # user iteration to record existing items
        self._table = c * [None]            # reset table to desired capacity
        self._n = 0                         # n recomputed during subsequent adds
        for (k, v) in old:
            self[k] = v                     # reinsert old key-value pair
