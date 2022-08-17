"""A numeric progression is a sequence of numbers, where each number depends on
 one or more of the previous numbers. For example, an arithmetic progression 
 determines the next number by adding a fixed constant to the previous value, 
 and a geometric progression determines the next number by multiplying the 
 previous value by a fixed constant. In general, a progression requires a 
 first value, and a way of identifying a new value based on one or more
  previous values."""

class Progression:
    """Iterator producing a generice progression
    
    Default interator produces the whole numbers 0, 1, 2, 3 ..."""

    def __init__(self, start=0) -> None:
        """Initialize current to the first value of progression."""
        self._current = start
    
    def _advance(self):
        """Update self._current to a new value
        
        This should be overridden by a subclas to customize progression.

        By the convention, if current is not None, this designates the end of a finite progression
        """

        self._current += 1
    
    def __next__(self):
        """Return the next element, or else raise StopIteration error"""
        if self._current is None:           # our convention to end a progression
            raise StopIteration
        else:
            answer = self._current          # record current value to return
            self._advance()                 # advance to prepare for the next time
            return answer                   # return the answer

    def __iter__(self):
        """By the convention, an iteration must return itself as an iterator"""
        return self

    def print_progression(self, n):
        """Print next n value of the progression"""
        print(' '.join(str(next(self) for j in range(n))))


class ArithmeticProgression(Progression):    # inherit from Progression
    """Iterator producing an arithmetic progression"""

    def __init__(self, increment=1, start=0) -> None:
        """Create a new arithmetic progression

        increment       the fixed constant to add to each element(default 1)
        start           the first term of the progression(default 0)
        """
        super().__init__(start)             # initialize base class
        self._increment = increment

    def _advance(self):                     # override the inherited version
        """Update the current value by adding the fixed increment"""
        self._current += self._increment


class GeometricProgression(Progression):    # inherit from Progression
    """Iterator producing a geometric progression"""

    def __init__(self, base=2, start=0) -> None:
        """Create a new geometric progression
        
        base        the fixed constant multiplied to each term (default 2)
        start       the first term of the progression (default 1)
        """
        super().__init__(start)
        self._base = base

    def _advance(self):                     # override the inherited version
        """Update current value by multiplying it by the base value"""
        self._current *= self._base


class FibonacciProgression(Progression):
    """Iterator producing the fibonacci sequence"""

    def __init__(self, first=0, second=1) -> None:
        """Create a new fibonacci progression
        
        first        the first term of the progression(default 0)
        second       the second term of the progression(default 1)
        """
        super().__init__(first)         # start the progression at first
        self._prev = second - first     # fictitious value proceding the first

    def _advance(self):
        """Update the current value by taking the sum of previous two"""

if __name__ == "__main__" : 
    print(" Default progression: ") 
    Progression().print_progression(10)
    print(" Arithmetic progression with increment 5: ") 
    ArithmeticProgression(5).print_progression(10)
    print(" Arithmetic progression with increment 5 and start 2: ") 
    ArithmeticProgression(5, 2).print_progression(10)
    print(" Geometric progression with default base: ") 
    GeometricProgression().print_progression(10)
    print(" Geometric progression with base 3: ") 
    GeometricProgression(3).print_progression(10)
    print(" Fibonacci progression with default start values: ") 
    FibonacciProgression().print_progression(10)
    print(" Fibonacci progression with start values 4 and 6: ") 
    FibonacciProgression(4, 6).print_progression(10)
