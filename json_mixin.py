import json
import collections

class JSONable( collections.abc.Mapping, collections.abc.Hashable):
    @property
    def json( self):
        return json.dumps( dict( sorted( self.items())))

    def from_json( json_string):
        return JSONRecord(json.loads( json_string))

    def __hash__(self):
        return hash( self.json)

    def __eq__(self, other):
        return self.json == other.json

    def __str__( self):
        return f"JSON-able object with {len( self)} attributes."

class JSONRecord( collections.UserDict, JSONable):
    def __repr__( self):
        return f"JSONRecord({repr( self.data)})"

class JSONCollection( collections.abc.MutableSet):
    '''

    Methods for MutableSet:
        __contains__, __iter__, __len__, add, discard

    Other Methods:
        __init__, __repr__, __str__, json

    '''
    def __init__( self, data=set()):
        self.data = set(data)

    def __repr__( self):
        return f"JSONCollection(data={list( self.data)})"

    def __str__( self):
        return f"JSON Data Set with {len( self)} items."

    @property
    def json( self):
        return f"[{','.join( [d.json for d in self.data])}]"
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
        if isinstance( item, JSONable):
            self.data.add(item)
        elif isinstance( item, str):
            self.data.add( JSONRecord.from_string( item))
        else:
            self.data.add( JSONRecord( item))

    def discard(self, item):
        self.data.pop(item)
    #
    #   End of MutableSet methods
    #
