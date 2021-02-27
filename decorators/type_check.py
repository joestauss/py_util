# Not tested yet.

class type_check:
    def __init__( self, types):
        self.types = types

    def __call__( self, function):
        @functools.wraps( function)
        def decorated( *args, **kwargs):
            assert len( args) == len( self.types)
            for (a, t) in zip(args, types):
                if not isinstance(a, t):
                    raise ValueError( "Explicit type-check has failed.")
            return function( *args, **kwargs)
        return decorated
