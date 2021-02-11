import collections.abc
from py_util.classes import BaseCollection

class BaseSet( collections.abc.MutableSet, BaseCollection):
    '''BaseSet is the base-class for unordered collections.

    MutableSet Abstract Methods
    --------------------------------
        __contains__, __iter__, __len__, add, discard

    MutableSet Mixin Methods
    -----------------------------
        from Set: __le__, __lt__, __eq__, __ne__, __gt__, __ge__,
                  __and__, __or__, __sub__, __xor__, isdisjoint
        also: clear, pop, remove, __ior__, __iand__, __ixor__, __isub__

    Other Methods
    -------------
        __init__, __str__, __repr__ (from BaseCollection)

    '''

    def __init__( self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        temp_data = self.data
        self.data = set()
        for item in temp_data:
            self.add( item)

    #   Start of MutableSet methods (some are already added by BaseCollection)
    #
    def add(self, item):
        self.data.add(item)

    def discard(self, item):
        self.data.remove(item)
    #
    #   End of MutableSet methods
