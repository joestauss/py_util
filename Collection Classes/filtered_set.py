import abc
import collections.abc
from utility import common_repr

@common_repr
class FilteredSet( collections.abc.MutableSet, abc.ABC):
    """A FilteredSet rejects some additions, based upon the filter method.
    """ #v1
    @abc.abstractmethod
    def filter( self, item):
        pass

    def __init__( self, data):
        self.data = set()
        for item in data:
            self.add( item)

    @property
    def _repr_args( self):
        return [ repr( self.data)]

    #   Start of MutableSet methods.
    #
    def __contains__(self, item):
        return item in self.data

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def add(self, item):
        if self.filter( item):
            self.data.add(item)

    def discard(self, item):
        self.data.pop(item)
    #
    #   End of MutableSet Methods
