def common_repr( cls):

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
