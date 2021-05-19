import collections.abc
from py_util.decorators import common_repr

@common_repr
class BaseCollection( collections.abc.Collection):
    '''BaseCollection is the parent of all other base collection classes.

    Collection Abstract Methods
    ---------------------------
        __contains__
        __iter__
        __len__

    Other methods
    -------------
        __init__
        __repr__ (through common_repr; re-implement properties to over-write)
        __str__
    '''

    def __init__( self, *args, **kwargs):
        if len(args) == 0:
            self.data = set()
        elif len(args) >= 1:
            self.data = args[0]
        if 'name' in kwargs:
            self.name = kwargs['name']
        else:
            self.name = f"Nameless {type( self).__name__}"

    @property
    def _repr_args( self):
        if self.data:
            return [ repr( self.data)]
        else:
            return []

    @property
    def _repr_kwargs( self):
        return { 'name' : self.name }

    def __str__( self):
        return f"{type( self).__name__}: {self.name} (len: {len( self)})"

    #   Beginning of Collection methods.
    #
    def __contains__(self, item):
        return item in self.data

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)
    #
    #   End of Collection methods.

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

class BaseSequence( collections.abc.MutableSequence, BaseCollection):
    '''BaseSequence is the base-class for ordered collections.

    MutableSequence Abstract Methods
    --------------------------------
        __getitem__, __setitem__, __delitem__, __len__, insert

    MutableSequence Mixin Methods
    -----------------------------
        from Sequence: __contains__, __iter__, __reversed__, index, count
        also: append, reverse, extend, pop, remove, __iadd__

    Other Methods
    -------------
        __init__, __str__, __repr__ (from BaseCollection)
    '''

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        try:
            self.data = list( self.data)
        except:
            raise ValueError( f"BaseSequence cannot be initialized.")

    #   Start of BaseSequence methods
    #   __len__ is implemented in BaseCollection.
    #
    def __setitem__(self, index, value):
        self.data[index] = value

    def __getitem__(self, index):
        return self.data[index]

    def __delitem__(self, index):
        del self.data[index]

    def insert(self, index, value):
        self.data.insert(index, value)
    #
    #   End of BaseSequence methods

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

    #   Start of MutableSet methods
    #       (__len__, __contains__, and __iter__ are added by BaseCollection)
    #
    def add(self, item):
        self.data.add(item)

    def discard(self, item):
        self.data.remove(item)
    #
    #   End of MutableSet methods
