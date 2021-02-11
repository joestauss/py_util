import collections.abc
from py_util.classes import BaseCollection

class BaseSet( collections.abc.MutableSet, BaseCollection):
    """A simple concrete class representing a collection of records.  Used for testing micins.""" #v1
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
