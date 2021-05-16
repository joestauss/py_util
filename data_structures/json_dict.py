import collections.abc
import json
import pathlib

class CommonMethodsMixin:
    def __init__(self, path):
        if not isinstance( path,  pathlib.Path):
            raise ValueError( "This class must be initialized with a pathlib.Path object.")
        elif not path.exists():
            with open( path, 'w') as fh:
                fh.write( "{}")
            print( f'I just created {path.name}!')
        self.path = path

    @property
    def as_json( self):
        with open( self.path) as fh:
            return json.dumps( json.load( fh), indent=6 )

    def __getitem__( self, item):
        with open( self.path) as fh:
            return json.load( fh)[ item]

    def __iter__( self):
        with open( self.path) as fh:
            return iter( json.load( fh))

    def __len__( self):
        with open( self.path) as fh:
            return len( json.load( fh))

class ReadOnlyJSONDict( CommonMethodsMixin, collections.abc.Mapping):
    pass

class JSONDict( CommonMethodsMixin, collections.abc.MutableMapping):
    def __setitem__( self, key, value):
        with open( self.path, 'r') as fh:
            data = json.load( fh)
        data[ key] = value
        with open( self.path, 'w') as fh:
            json.dump( data, fh, indent=6)

    def __delitem__( self, key):
        with open( self.path, 'r') as fh:
            data = json.load( fh)
        del data[ key]
        with open( self.path, 'w') as fh:
            json.dump( data, fh, indent=6)
