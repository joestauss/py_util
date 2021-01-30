class BaseRecord( collections.UserDict):
    """A simple concrete record class for testing mixins.""" #v1
    def __init__( self, *args, **kwargs):
        super().__init__( *args, **kwargs)

    def __repr__( self):
        return f"{type(self).__name__}({repr( self.data)})"

    def __str__( self):
        return f"This is a {type(self).__name__} with {len( self.data)} items."

    def __hash__( self):
        return hash( repr( self))

class BaseCollection( collections.abc.MutableSet):
    """A simple concrete class representing a collection of records.  Used for testing micins.""" #v1
    def __init__( self, *args, **kwargs):
        self.data = set()
        if len(args) > 0:
            init_data = set(args[0])
            for record in init_data:
                self.add( record)
        if 'name' in kwargs:
            self.name = kwargs['name']
        else:
            self.name = "Nameless BaseCollection"

    def __repr__( self):
        return f"{type(self).__name__}({list( self.data)}, name={repr(self.name)})"

    def __str__( self):
        return f"This is a {type(self).__name__} with {len( self)} items."
    #
    #   Start of MutableSet methods
    #
    def __contains__(self, item):
        return item in self.data

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def add(self, item):
        if isinstance( item, BaseRecord):
            self.data.add(item)
        else:
            raise ValueError( "Tried to add a non-BaseRecord item to a BaseCollection.")

    def discard(self, item):
        self.data.pop(item)
    #
    #   End of MutableSet methods
    #
