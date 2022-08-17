from unsortedTableMap import UnsortedTableMap
from hashMapBase import HashMapBase


class ChainHashMap(HashMapBase):
    """Hash map implemented with separate chaining for collision resolution"""

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('key error: ' + repr(k))     # no match found
        return bucket[k]                                # may raise key error

    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()     # bucket is new to the table
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:           # key was new to the table
            self._n += 1                            # increase overall map size

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('key error: ' + repr(k))     # no match found
        del bucket[k]                                # may raise key error

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key
