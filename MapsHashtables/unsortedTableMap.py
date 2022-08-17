from mapBase import MapBase


class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list"""

    def __init__(self):
        """Create an empty map"""
        self._table = []        # list of _Item's

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)"""
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('key error: ' + repr(k))

    def __setitem__(self, key, value):
        """Assign value v to key k, overwriting existing value if present"""
        for item in self._table:
            if key == item._key:
                item._value = value         # found a match, reassign value
                return                      # and quit
        # did not find a match for key
        self._table.append(self._Item(key, value))

    def __delitem__(self, key):
        """Remove item associated with key 'key' raise KeyError if not found"""
        for j in range(len(self._table)):
            if key == self._table[j]._key:      # found a match
                self._table.pop(j)              # remove item
                return
        raise KeyError('key error: ' + repr(key))

    def __len__(self):
        """Return number of items in the map"""
        return len(self._table)

    def __iter__(self):
        """Generate iteration of the map's keys"""
        for item in self._table:
            yield item._key