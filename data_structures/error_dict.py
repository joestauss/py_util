import collections.abc

class ErrorDict( collections.abc.MutableMapping):
    '''
This class was first implemented to be the default dictionary for a MultiDict,
so it was written to work with that class.  T
    '''
    def __getitem__( self, key):
        raise TypeError( "This dictionary is unable to be queried.")

    def __setitem__( self, key, value):
        raise TypeError( "This dictionary is unable to be altered.")

    def __delitem__( self, key):
        raise TypeError( "This dictionary is unable to be altered.")

    def __len__( self):
        return 0

    def __iter__( self):
        return iter( list())
