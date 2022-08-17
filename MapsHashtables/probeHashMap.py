
from hashMapBase import HashMapBase


class ProbeHashMap(HashMapBase):
    """hash map implemented with linear probing for collision resolution"""
    _AVAIL = object()           # sentinel marks location of previous deletions

    def is_available(self, j):
        """Return True if index j is available in the table"""
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        """Search for key k in bucket at index j

        Return success, index tuple described as follows
        if match was found, success is True and index denotes its location
        if no match found, success is False and index denotes it's first available slot
        """
        firstAvail = None
        while True:
            if self.is_available(j):
                if firstAvail is None:
                    firstAvail = j          # mark this as first avail
                if self._table[j] is None:
                    return False, firstAvail        # search has failed
            elif k == self._table[j]._key:
                return True, j                      # found a match
            j = (j + 1) % len(self._table)      # keep looking

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('key error: ' + repr(k))  # no match found
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k, v)
            self._n += 1
        else:
            self._table[s]._value = v

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('key error: ' + repr(k))  # no match found
        self._table[s] = ProbeHashMap._AVAIL

    def __iter__(self):
        for j in range(len(self._table)):           # scan entire table
            if not self.is_available(j):
                yield self._table[j]._key
