"""
This implementation relies on two advanced Python techniques. The first is that 
we declare the ABCMeta class of the abc module as a metaclass of our Sequence class.
A metaclass is different from a superclass, in that it provides a template for the 
class definition itself. Specifically, the ABCMeta declaration assures that the 
constructor for the class raises an error.
The second advanced technique is the use of the @abstractmethod decorator 
immediately before the     len     and     getitem     methods are declared. 
That de- clares these two particular methods to be abstract, meaning that we do 
not provide an implementation within our Sequence base class, but that we expect 
any concrete subclasses to support those two methods. Python enforces this 
expectation, by dis- allowing instantiation for any subclass that does not 
override the abstract methods with concrete implementations.
"""

from abc import ABCMeta, abstractmethod    # need these definitions

class Sequence(metaclass=ABCMeta):
    """Our own version of collectio.Sequence abstract base class"""

    @abstractmethod
    def __len__(self):
        """return length of the sequence"""

    @abstractmethod
    def __getitem__(self, __o):
        """return jth element of the sequence"""

    def __contains__(self, __o):
        """return True if value is found in the sequence or raise ValueError"""
        for j in range(len(self)):
            if self[j]==__o:
                return True
        return False

    def index(self, __o):
        """return the left most index at which value is found or raise ValueError"""
        for j in range(len(self)):
            if self[j]==__o:
                return j
        raise ValueError('value not in the sequence')

    def count(self, __o):
        """return the number of elements equal to the given value"""
        k = 0
        for j in range(len(self)):
            if self[j]==__o:
                k+=1
        return k