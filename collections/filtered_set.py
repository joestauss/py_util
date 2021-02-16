import abc
#from py_util.collections import BaseSet
import collections.abc

class FilteredSet( collections.abc.MutableSet, abc.ABC):
    """A FilteredSet rejects some additions, based upon the filter method.
    """ #v1
    @abc.abstractmethod
    def filter( self, item):
        pass

    def add(self, item):
        if self.filter( item):
            super().add(item)
