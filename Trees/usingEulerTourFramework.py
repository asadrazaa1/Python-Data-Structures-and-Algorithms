import re
from time import sleep


class EulerTour:
    """Abstract base class for performing Euler tour of a tree
    
    _hoo_previsit and _hook_postvisit may be overridden by subclasses
    """
    def __init__(self, tree) -> None:
        """Prepare an Euler tour template for given tree"""
        self._tree = tree

    def tree(self):
        """Return reference to the tree being traversed"""
        return self._tree
    
    def execute(self):
        """Perform the tour and return the any result from post visit of root"""
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])     # start recusions
    
    def _tour(self, p, d, path):
        """Perfomr tou of subtree rooted at Position p
        
        p       Postion of current being visited
        d       depth of p in the tree
        path    list of indices of children on path from root to p
        """
        self._hook_previsit(p, d, path)     # pre visit p
        results = []
        path.appen(0)                       # add new index to end of path before recusion
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path))        # Recursion on child's subtree
            path[-1] += 1       # increment index
        path.pop()              # remove index from end of the path
        answer = self._hook_postvisit(p, d, path, results)  # post visit p
        return answer
    
    def _hook_previsit(self, p, d, path):       # can be overridden
        pass

    def _hook_postvisit(self, p, d, path, results):       # can be overridden
        pass


class PreorderPrintIndentedTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        print(2*d*'' + str(p.element()))


class PreoderPrintIndentedLabeledTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        label = '.'.join(str(j+1) for j in path)    # labels are on indexed
        print(2*d*'' + label, str(p.element()))


class ParenthesizeTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        if path and path[-1]>0:     # p follows a sibling
            print(', ', end='')      # preface with comma
        print(p.element(), end='')    # print element
        if not self.tree().is_leaf(p):  # if p has children
            print(' (', end='')         # print openning parenthesis

    def _hook_postvisit(self, p, d, path, results):
        if not self.tree().is_lead(p):  # if p has children
            print(')', end='')          # print closing parenthesis


class DiskSpaceTour(EulerTour):
    def _hook_postvisit(self, p, d, path, results):
        # simply add space associated with p to that of it's subtrees
        return p.element().space() + sum(results)