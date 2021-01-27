import collections
import json
from json_mixin import JSONable

class Taggable():
    def __init__( self, *args, tags=set(), **kwargs):
        super().__init__(*args, **kwargs)
        self.tags = tags

    def tag( self, tag):
        """Add the parameter to this TaggableRecord's "tags" set."""
        self.tags.add( tag)

class TaggableRecord(Taggable, JSONable, collections.UserDict):
    def __init__( self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__( self):
        return f"TaggableRecord({repr( self.data)})"

class TaggableCollection( collections.abc.MutableSet):
    '''

    Methods for MutableSet:
        __contains__, __iter__, __len__, add, discard

    Other Methods:
        __init__, __repr__, __str__, tags, tag_all

    '''
    def __init__( self, data=set(), name='Taggable Dataset'):
        self.data = set(data)
        for record in data:
            self.add( record)
        self.name = name

    def __repr__( self):
        return f"TaggableCollection(data={list( self.data)}, name={repr(self.name)})"

    def __str__( self):
        return f"Taggable Data Set with {len( self)} items."

    @property
    def tags( self):
        """Return all the tags that are on any record."""
        all_tags = set()
        for record in self.data:
            all_tags = all_tags | record.tags
        return all_tags

    def tag_all( self, tag):
        """Apply a tag to each of the records."""
        for record in self.data:
            if isinstance( record, TaggableRecord):
                record.tag( tag)
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
        if isinstance( item, Taggable):
            if item in self.data:
                for record in self.data:
                    if record == item:
                        record.tags = record.tags | item.tags
            else:
                self.data.add(item)
        else:
            raise ValueError( "Tried to add a non-taggable item to a TaggableCollection.")

    def discard(self, item):
        self.data.pop(item)
    #
    #   End of MutableSet methods
    #

if __name__ == '__main__':
    help( TaggableDataset)
