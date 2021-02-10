import collections.abc
import abc
import json

class JSONableMapping( collections.abc.Mapping, collections.abc.Hashable, abc.ABC):
    """A JSONable mapping can be represented in JSON or initialized from json.

    A JSONable class must be initializable with ClassName( data_dictionary).  In return it gets...
    * obj.json                    : a property thay returns the object as a JSON string
    * cls.from_json( json_string) : a method that initializes the object from the string.
    * The object is also made hashable by the result of obj.json.

    This is an abstract class and should work with any implementation of Mapping.
    """ #v1
    @abc.abstractmethod
    def __init__( self, data_dictionary, *args, **kwargs):
        """An __init__ method must be callable in this format for cls.from_json."""
        raise NotImplementedError

    @property
    def json( self):
        """Return a JSON representation of the object."""
        def replace_empty_with_none( item):
            if not item:
                return None
            return item
        return json.dumps( { k: replace_empty_with_none(v) for k, v in self.items()})

    def __hash__(self):
        """Return a hash value based on the JSON representation of the object."""
        return hash( self.json)

    def __repr__( self):
        self_as_str = '{' + ', '.join( [ f"{repr( k)} : {repr( v)}" for k, v in self.items()]) + '}'
        return f"{type(self).__name__}({self_as_str})"

    @classmethod
    def from_json( cls, json_string):
        """Create an instance of the object from a JSON string."""
        return cls( json.loads(json_string))
