class Tree:
    """Abstract base class representing a tree structure"""

    # __________________ nested Position class __________________
    class Position:
        """An abstraction representing the location of a single element"""

        def element(self):
            """Return the element stored at this Position"""
            raise NotImplementedError("must be implemented by the subclass")
        
        def __eq__(self, __o: object) -> bool:
            """Return True if __o represent the smae Position"""
            raise NotImplementedError("must be implemented by the subclass")
        
        def __ne__(self, __o: object) -> bool:
            """Return True if __o does not represent the same Position"""
            raise NotImplementedError("must be implemented by the subclass")
            
    # __________________ abstract methods that concrete subclass must support __________________
    def root(self):
        """Return Position representing the tree's root (or None if empty)"""
        raise NotImplementedError("must be implemented by the subclass")
    
    def parent(self, p):
        """Return Position representing p's parent ( or None if empty)"""
        raise NotImplementedError("must be implemented by the subclass")
    
    def num_children(self, p):
        """Return the number of children Position p has"""
        raise NotImplementedError("must be implemented by the subclass")

    def children(self, p):
        """Generate an iteration of Positions representing p's children"""
        raise NotImplementedError("must be implemented by the subclass")
    
    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError("must be implemented by the subclass")

    # __________________ concrete methods implemented in this class __________________
    def is_root(self, p):
        """Return True if Position p is root of the tree"""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children"""
        return self.num_children() == 0
    
    def is_empty(self):
        """Return True if the tree is empty"""
        return len(self) == 0
