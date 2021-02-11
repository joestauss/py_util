import collections.abc
from py_util.classes import BaseCollection

class BaseMapping( collections.abc.MutableMapping, BaseCollection):
    def __init__( self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        if not self.data:
            self.data = {}
        if not isinstance( self.data, dict):
            raise ValueError( "A mapping can only be inititalized with a dictionary.")

    #   Start of MutableMapping methods
    #   __init__ and __len__ are implmented by BaseCollection
    #
    def __getitem__( self, key):
        return self.data[ key]

    def __setitem__( self, key, value):
        self.data[ key] = value

    def __delitem__( self, item):
        self.data.pop( item)
    #
    #   End of MutableMapping methods
