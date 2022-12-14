from MapsHashtables.sortedTableMap import SortedTableMap


class CostPerformanceDatabase:
    """Maintain a database of maximanl (cost, performance) pairs"""

    def __init__(self):
        """Create an empty database"""
        self._M = SortedTableMap()  # or a more efficient sorted map

    def best(self, c):
        """Return cost, performance pair with the largest cost not exceeding c

        Return None if there is no such pair
        """
        return self._M.find_le(c)

    def add(self, c, p):
        """Add new entry with cost c and performance p"""
        # determine if c, p is dominated by an existing pair
        other = self._M.find_le(c)      # other is at least as cheap as c
        if other is not None and other[1] <= p:
            del self._M[other[0]]
            other = self._M.find_gt(c)
