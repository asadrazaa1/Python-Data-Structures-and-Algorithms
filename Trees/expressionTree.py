from linkedBinaryTree import LinkedBinaryTree


class ExpressionTree(LinkedBinaryTree):
    """An arithmetic expression Tree"""

    def __init__(self, token, left=None, right=None):
        """Create an expression tree

        In a single parameter form, token should be a leaf value (e.g., 42 ),
        and the expression tree will have that value at an isolated node.

        In a three-parameter version, token should be an operator,
        and left and right should be existing ExpressionTree instances
        that become the operands for the binary operator.
        """

        super().__init__()      # linkedBinaryTree initialization
        if not isinstance(token, str):
            raise TypeError('token must be string')
        self._add_root(token)       # user inherited, nonpublic method
        if left is not None:        # presumably three parameter form
            if token not in '+-*x/':
                raise ValueError('token must a valid operator')
            self._attach(self.root(), left, right)      # user inherited, nonpublic method

    def __str__(self):
        """Return string representation of the expression"""
        pieces = []                                     # sequence of piecewise strings to compose
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)

    def _parenthesize_recur(self, p, result):
        """Append piecewise representation of p's subtree to resulting list"""
        if self.is_leaf(p):
            result.append(str(p.element()))             # lead value as string
        else:
            result.append('(')                          # opening parenthesis
            self._parenthesize_recur(self.left(p), result)  # left subtree
            result.append(p.element())                  # operator
            self._parenthesize_recur(self.right(p), result)     # right subtree
            result.append(')')          # closing parenthesis























