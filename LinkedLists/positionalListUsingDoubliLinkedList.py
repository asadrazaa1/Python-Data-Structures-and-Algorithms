

class _DoublyLinkedBase:
    """A base class providing a doubly linked list implementation."""

    class _Node:
        """Lightweigh, nonpublic class for storing a doubly linked node"""
        __slots__ = '_element', '_prev', '_next'        # streamline memory

        def __init__(self, element, prev, next) -> None:# initlize the node's fields
            self._element = element                     # user's elements
            self._prev = prev                           # previous node reference
            self._next = next                           # next node reference
    
    def __init__(self) -> None:
        """Create an empty list"""
        self._header = self._Node(None, None, None)     
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer              # trailer is after header
        self._trailer._prev = self._header              # header is before trailer
        self._size = 0                                  # number of elements

    def __len__(self):
        """Return the number of elements in the list"""
        return self._size
    
    def is_empty(self):
        """Return True is list is emtpy otherwise False"""
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node"""
        newest = self._Node(e, predecessor, successor)      # linked two neighbours
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return it;s element"""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element                         # record deleted element
        node._prev = node._next = node._element = None  # deprecate node
        return element                                  # return deleted element

    
class PositionalList(_DoublyLinkedBase):                   # using inheritance
    """A sequential container of elements allowing positional access"""
    #_______________ nested Postion class _______________
    class Position:
        """An abstraction representing the location of a single element"""
        def __init__(self, container, node) -> None:
            """Contructor should not be invoked by a user"""
            self._container = container
            self._node = node
        
        def element(self):
            """Return the element stored at this Position"""
            return self._node._element
        
        def __eq__(self, __o: object) -> bool:
            """Return True of __o is a Position representing the same location"""
            return type(__o) is type(self) and __o._node is self._node

        def __ne__(self, __o: object) -> bool:
            """Return True if other does not represent the same location"""
            return not(self == __o)
    #_______________ utility methods _______________
    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Postion Type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:                      # deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return position instance for given node(or None if sentinel)"""
        if node is self._header or node is self._trailer:
            return None                                 # boundry violation
        return self.Position(self, node)                # legitimate position
    #_______________ accessors _______________
    def first(self):
        """Return the first Postion in the list (or None if list is empty)"""
        return self._make_position(self._header._next)
    
    def last(self):
        """Return the last Position in the list (or None if list is empty)"""
        return self._make_position(self._trailer._prev)
    
    def before(self, p):
        """Return the Position in the list just before p (or None if p is first))"""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Return the Postion just after p (or None if p is last)"""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.firs()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
    #_______________ mutators _______________
    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        """Add element between existing nodes and return new Position."""
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)
    
    def add_first(self, e):
        """Insert element e at the front of the list and return new Position"""
        return self._insert_between(e, self._header, self._header._next)
    
    def add_last(self, e):
        """Add element e at the back of the list and return new Position"""
        return self._insert_between(e, self._trailer._prev, self._trailer)
    
    def add_before(self, p, e):
        """Insert element e into the list before Position p an return new Position"""
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Add element e into the list after Position p and return new Positionn"""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at the Position p"""
        original = self._validate(p)
        return self._delete_node(original)      # inherited method returns element
    
    def replace(self, p, e):
        """Replace the element at the Position p with e
        
        Return the element formerly at Position p.
        """
        original = self._validate(p)
        old_value = original._element           # temporarily store old element
        original._element = e                   # replace with new element
        return old_value                        # return the old element value
