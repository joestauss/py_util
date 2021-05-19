import collections.abc
from py_util.data_structures import BaseCollection

class BaseMapping( collections.abc.MutableMapping, BaseCollection):
    '''BaseMapping is mostly used for record-type objects.

    MutableMapping Abstract Methods
    -------------------------------
        __getitem__, __setitem__, __delitem__, __iter__, __len__

    MutableMapping Mixin Methods
    ----------------------------
        from Mapping: __contains__, __eq__, __ne__,
                      keys, items, values, get
        also: pop, popitem, clear, update, setdefault

    Other Methods
    -------------
        __init__, __str__, __repr__ (from BaseCollection)

    '''

    def __init__( self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        if not self.data:
            self.data = {}
        if not isinstance( self.data, dict):
            raise ValueError( "A mapping can only be inititalized with a dictionary.")

    #   Start of MutableMapping methods
    #   __iter__ and __len__ are implmented by BaseCollection
    #
    def __getitem__( self, key):
        return self.data[ key]

    def __setitem__( self, key, value):
        self.data[ key] = value

    def __delitem__( self, item):
        self.data.pop( item)
    #
    #   End of MutableMapping methods
