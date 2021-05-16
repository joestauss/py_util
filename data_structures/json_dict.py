import collections.abc
import json

class ReadOnlyJSONDict( collections.abc.Mapping):
    '''Read-only JSON Dictionary

    collections.abc.Mapping
    -----------------------
        required: __getitem__, __iter__, __len__
        acquired: __contains__, __eq__, __ne__, keys, items, values, get

    Other Methods
    -------------
        __init__
        as_json (property)
    '''
    def __init__(self, path):
        self.__path = path

    def __getitem__( self, item):
        with open( self.__path) as fh:
            return json.load( fh)[ item]

    def __iter__( self):
        with open( self.__path) as fh:
            return iter( json.load( fh))

    def __len__( self):
        with open( self.__path) as fh:
            return len( json.load( fh))

    @property
    def as_json( self):
        with open( self.__path) as fh:
            return json.dumps( json.load( fh), indent=6 )

class JSONDict( collections.abc.MutableMapping, ReadOnlyJSONDict):
    #__setitem__, __delitem__,
    def __set__( self, key, value):
        with open( self.__path) as fh:
            data = json.load( fh)
        data[ key] = value
        json.dump( data, self.__path, indent=6)

    def __delitem__( self, key):
        with open( self.__path) as fh:
            data = json.load( fh)
        del data[ key]
        json.dump( data, self.__path, indent=6)
