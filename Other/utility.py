import collections.abc

def common_repr( cls):
    """The @common_repr decorator adds the usual __repr__ method to a class.
    """ #v1
    def __repr__(self):
        args_string, kwargs_string = None, None
        if hasattr( self, '_repr_args'):
            args_string = ', '.join( self._repr_args)
        if hasattr( self, '_repr_kwargs'):
            kwargs_string = ', '.join( [f"{k}={v}" for k,v in self._repr_kwargs.items()])
        if args_string and not kwargs_string:
            return f"{type( self).__name__}({args_string})"
        if kwargs_string and not args_string:
            return f"{type( self).__name__}({kwargs_string})"
        if args_string and kwargs_string:
            return f"{type( self).__name__}({args_string}, {kwargs_string})"
        return f"{type(self).__name__}()"
    cls.__repr__ = __repr__
    return cls

@common_repr
class BaseSequence( collections.abc.MutableSequence):
    def __init__(self, *args):
        if args:
            self.data = list( args[0])
        else:
            self.data = []

    def __setitem__(self, index, value):
        self.data[index] = value

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return len(self.data)

    def __delitem__(self, index):
        del self.data[index]

    def insert(self, index, value):
        self.data.insert(index, value)

    def __str__(self):
        return "\n".join( [str(item) for item in self.data])


    @property
    def _repr_args( self):
        return [ repr( self.data)]
