
class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""


    """______________________nested _Node class______________________"""
    class _Node:
        """Lightweight, non public class for storing a singly linked list."""
        __slots__ = '_element', '_next'             # streamline memory usage

        def __init__(self, element, next) -> None:  # initialize node's fields
            self._element = element                 # reference to user's element
            self._next = next                       # reference to next node

    """______________________Queue methods______________________""" 
    def __init__(self) -> None:
        """Create an empty queue"""
        self._head = None                           # reference to the head node
        self._tail = None
        self._size = 0                              # number of queue elements

    def __len__(self):
        """Return the number of elements in the queue"""
        return self._size

    def is_empty(self):
        """Return True if queue is empty othereise False."""
        return self._size == 0
    
    def enqueue(self, e):
        """Add element e to the back of the queue."""
        newest = self._Node(e, None)      # node will be new tail node
        if self.is_empty():
            self._head = newest           # special case: previously empty
        else:
            self._tail._next = newest   
        self._tail = newest               # update reference to the tail node
        self._size += 1
    
    def first(self):
        """Return (but do not remove) the element at the front of the queue
        
        Raise empty exception if the queue is emtpy.
        """
        if self.is_empty():
            raise Empty("queue is empty")
        return self._head._element                  # top of the queue is at the head of the list
    
    def dequeue(self):
        """Remove and return the first element from the queue (i.e FIFO).
        
        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty("queue is empty")
        answer = self._head._element
        self._head = self._head._next              
        self._size -= 1
        if self.is_empty():                         # special case , queue is emtpy
            self._tail = None                       # removed head had been the tail
        return answer

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


class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure"""

    # ____________________ additional abstract methods ____________________
    def left(self, p):
        """Return a Position representing p's left child
        
        Return None if p does not have a left child
        """
        raise NotImplemented("must be implemented by the subclass")

    def right(self, p):
        """Return a Position representing p's right child
        
        Return None if p does not have a right child
        """
        raise NotImplemented("must be implemented by the subclass")
    
    # ____________________ concrete methods implemented in this class ____________________
    def sibling(self, p):
        """Return a Position representing p's sibling (or None if no sibling)"""
        parent = self.parent(p)
        if parent is None:                      # p must the root
            return None                         # root has no siblings
        else:
            if p == self.left(parent):
                return self.right(parent)       # possibly None
            else:
                return self.left(parent)        # possibly None

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure"""

    class _Node:            # lightweight, nonpublic class for storing a node
        __slots__ = '_element', '_parent', '_left', '_right'
        
        def __init__(self, element, parent=None, left=None, right=None) -> None:
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node) -> None:
            """Constrcutor should not be invoked by user."""
            self._container = container
            self._node = node
        
        def element(self):
            """Return the element stored at this Position"""
            return self._node._element
        
        def __eq__(self, __o: object) -> bool:
            """Return True if other is a Position representing the same location."""
            return type(__o) == type(self) and __o._node is self._node

    def _validate(self, p):
        """Return associated node, if position is valid"""
        if not isinstance(p, self.Position):
            raise TypeError("p must be a proper Position type")
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._parent is p._node:              # for deprecated nodes
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)"""
        return self.Position(self, node) if node is not None else None
    
    # ____________________ binary tree constructor ____________________
    def __init__(self) -> None:
        """Create an initially empty binary tree"""
        self._root = None
        self._size = 0
    
    # ____________________ public accessors ____________________
    def __len__(self):
        """Return the total number of elements in the tree"""
        return self._size
    
    def root(self):
        """Return the root Position of the tree (or None if tree is empty)"""
        return self._make_position(self._root)

    def parent(self, p):
        """Return the Position of p's parent (or None if tree is empy)"""
        node = self._validate(p)
        return self._make_position(node._parent)
    
    def left(self, p):
        """Return the Position of p's left child (or None if tree is empy)"""
        node = self._validate(p)
        return self._make_position(node._left)
    
    def right(self, p):
        """Return the Position of p's right child (or None if tree is empy)"""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of Position p"""
        node = self._validate(p)
        count = 0
        if node._left is not None:              # left child exists
            count += 1
        if node._right is not None:             # right child exists
            count += 1
        return count

    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position
        
        Raise ValueError if tree is nonempty
        """
        if self._root is not None: raise ValueError('root exists')
        self._size += 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """Create a new left child for Position p, storing element e
        
        Return the Position of new node.
        Raise ValueError if Position p is invalid or p already has a left child
        """
        node = self._validate(p)
        if node._left is not None: raise ValueError('left child exists')
        self._size += 1
        node._left = self._Node(e, node)                # node is its parent
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """Create a new right child for Position p, storing element e
        
        Return the Position of new node
        Raise ValueError if Position p is invalid or p already has a right child
        """
        node = self._validate(p)
        if node._right is not None: raise ValueError('eight child exists')
        self._size += 1
        node._right = self._Node(e, node)               # node is its parent
        return self._make_position(node._right)
    
    def _replace(self, p, e):
        """Replace the element at Position p with e and return old element"""

        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete the node at Postion p, and replace it with its child, if any
        
        Return the element that had been stored at Postion p
        Raise ValueError if Postion is p is invalid or p has two children
        """
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError('p has two children')
        child = node._left if node._right else node._right      # might be None
        if child is not None:
            child._parent = node._parent                        # child's grandparent becomes parent
        if node is self._root:
            self._root = child                                  # child becomes root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._seize -= 1
        node._parent = node                 # deprecated node
        return node._element
    
    def _attach(self, p, t1, t2):
        """Attach Trees t1 and t2 as left and right subtrees of external p."""
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2): # all three must be same type
            raise TypeError('tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():           # attach t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None             # set t1 instance to empty
            t1._size = 0
        if not t2.is_empty():           # attach t2 as right subtree of node
            t2._root._parent = node
            node._right = t2._root
            t2._root = None             # set t2 instance to empty
            t2._size = 0
    
    # ____________________ preoder traversals ____________________
    def preorder(self):
        """Generate preorder iteration of position in the tree"""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):       # start Recursion
                yield p
    
    def _subtree_preorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p."""
        yield p                                         # visit p before it;s subtrees
        for c in self.children(p):                      # for each child c
            for other in self._subtree_preorder(c):     # do preorder of c's subtree
                yield other                             # yielding each to our caller

    # ____________________ postorder traversals ____________________
    def postorder(self):
        """Generate preorder iteration of position in the tree"""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):       # start Recursion
                yield p
    
    def _subtree_postorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p."""
        for c in self.children(p):                      # for each child c
            for other in self._subtree_postorder(c):    # do preorder of c's subtree
                yield other                             # yielding each to our caller
        yield p                                         # visit p after it;s subtrees

    # ____________________ breadth first traversals ____________________
    def breadthfirst(self):
        """Generate a breadth first iteration of the positions of the tree"""
        if not self.is_empty():
            fringe = LinkedQueue()                      # known positios not yet yielded
            fringe.enqueue(self.root())                 # starting with root
            while not fringe.is_empty():
                p = fringe.dequeue()                    # remove from front of the queue
                yield p                                 # return this position
                for c in self.children(p):
                    fringe.enqueue(c)                   # add children to back of the queue

    # ____________________ inorder traversals ____________________
    def inorder(self):
        """Generate an inorder iteratiosn of position in the tree"""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):       # start Recursion
                yield p
    
    def _subtree_inorder(self, p):
        """Generate a inorder iteration of positions in subtree rooted at p."""
        if self.left(p) is not None:            # if left child exists traverse it's subtree
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p                                 # visit p between it's subtrees
        if self.right(p) is not None:            # if right child exists traverse it's subtree
            for other in self._subtree_inorder(self.right(p)):
                yield other

    # overrider inherited version make inorder the default
    def positions(self):
        """Generate an iteration of the tree's positions"""
        return self.inorder(self)