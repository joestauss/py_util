import collections.abc
import copy

class MultiDict( collections.abc.MutableMapping):
    def __init__( self, special_keys, default=dict()):
        self.special_keys = special_keys
        self.default      = default

    def __str__( self):
        return str( special_keys)

    def select_dict( self, key):
        for key_list, sub_dict in self.special_keys.items():
            if key in key_list:
                return sub_dict
        return self.default

    def __getitem__( self, key):
        return self.select_dict( key).__getitem__( key)

    def __setitem__( self, key, value):
        return self.select_dict( key).__setitem__( key)

    def __delitem__( self, item):
        return self.select_dict( key).__delitem__( key)

    def __len__( self):
        temp = copy.copy( self.default)
        for d in self.special_keys.values():
            temp.update( d)
        return len( temp)

    def __iter__( self):
        temp = copy.copy( self.default)
        for d in self.special_keys.values():
            temp.update( d)
        return iter( temp)

if __name__=="__main__":
    loud_vowels = {
        'A' : "AAAAAA",
        'E' : 'EEEEEE',
        'I' : "IIIIII",
        'O' : "OOOOOO",
        'U' : "UUUUUU"
    }
    sk = {
        ( 'A', 'E', 'I', 'O', 'U') : loud_vowels
    }
    md = MultiDict( sk, default={ 'A' : 'a', 'B' : 'b'} )
    print( md[ 'B'])
    print( len( md))
