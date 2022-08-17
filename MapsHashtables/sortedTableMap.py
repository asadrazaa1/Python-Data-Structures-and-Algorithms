from hashMapBase import HashMapBase


class SortedTableMap(HashMapBase):
    """Map implementation using a sorted table"""

    # ----------------------- nonpublic behaviours -----------------------
    def _find_index(self, k, low, high):
        """Return index of the leftmost item with key greater than or equal to k

        Return high + 1 if no such item qualifies

        That is, j will be returned such that :
            all items of slice table[low:j] have key < k
            all items of slice table[j:high+1] have key >= k
        """

        if high < low:
            return high + 1  # no element qualifies
        else:
            mid = (low + high) // 2
            if k == self._table[mid]._key:
                return mid  # found exact match
            elif k < self._table[mid]._key:
                return self._find_index(k, low, mid - 1)  # node may return exact mid
            else:
                return self._find_index(k, mid + 1, high)  # answer is right after mid

    # ----------------------- public behaviours -----------------------
    def __init__(self):
        """Create an empty map"""
        self._table = []

    def __len__(self):
        """Return number of items in the map"""
        return len(self._table)

    def __getitem__(self, item):
        """Return value associated with key k (raise key error if not found)"""
        j = self._find_index(item, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != item:
            raise KeyError('key error: ' + repr(item))
        return self._table[j]._value

    def __setitem__(self, key, value):
        """Assign value to key, overwriting existing value if present"""
        j = self._find_index(key, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == key:
            self._table[j]._value = value                       # assigning value
        else:
            self._table.insert(j, self._Item(key, value))       # adding new item

    def __delitem__(self, key):
        """Remove item associate with key k, raise KeyError if not found"""
        j = self._find_index(key, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != key:
            raise KeyError('key error ' + repr(key))
        self._table.pop(j)                                      # del item

    def __iter__(self):
        """Generate keys of the map ordered from minimum to maximum"""
        for item in self._table:
            yield item._key

    def __reversed__(self):
        """Generate keys of the map ordered from maximum to minimum"""
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        """Return key, value pair with minimum key or None if empty"""
        if len(self._table) > 0:
            return self._table[0]._key, self._table[0]._value
        else:
            return None

    def find_max(self):
        """Return key, value pair with maximum key or None if empty"""
        if len(self._table) > 0:
            return self._table[-1]._key, self._table[-1]._value
        else:
            return None

    def find_ge(self, k):
        """Return key, value pair with least key greater than or equal to k"""
        j = self._find_index(k, 0, len(self._table) - 1)        #j's key >= k
        if j < len(self._table):
            return self._table[j]._key, self._table[j]._value
        else:
            return None

    def find_le(self, k):
        """Return key, value pair with least key less than or equal to k"""
        j = self._find_index(k, 0, len(self._table) - 1)        #j's key >= k
        if j > len(self._table):
            return self._table[j]._key, self._table[j]._value
        else:
            return None

    def find_lt(self, k):
        """Return key, value pair with greatest key stricly less than k"""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j > 0:
            return self._table[j-1]._key, self._table[j-1]._value
        else:
            return None

    def find_gt(self, k):
        """Return key, value pair with greatest key stricly greater than k"""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            j += 1                                      # advanced past match
        if j < len(self._table):
            return self._table[j]._key, self._table[j]._value
        else:
            return None

    def find_range(self, start, stop):
        """Iterate all key, value pairs such that start <= key < stop

        if start is None, iteration begins with minimum key of map
        if stop is none, iteration continues through the maximum key of map
        """

        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self._table) - 1)    # first find result
            while j < len(self._table) and (stop is None or self._table[j]._key < stop):
                yield self._table[j]._key, self._table[j]._value
                j += 1
