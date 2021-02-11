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
        elif len(args) == 1:
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
