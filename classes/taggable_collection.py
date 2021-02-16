import collections.abc
from py_util.parsers import read_taggable_collection

class TaggableCollection( collections.abc.Collection):
    """A taggable class inherits the tags attribute and the following methods.

    Methods
    =======
        __init__
        tag
        tag_all

    Properties
    ==========
        all_tags
    """

    def __init__( self, *args, **kwargs):
        """Add the tags attribute."""
        super().__init__(*args, **kwargs)
        if 'tags' in kwargs:
            self.tags = kwargs['tags']
        else:
            self.tags = {}

    def tag( self, item, tag_string):
        """Add the parameter to this TaggableRecord's "tags" set."""
        if tag_string in self.tags:
            self.tags[ tag_string].append( item)
        else:
            self.tags[ tag_string] = [ item]

    @property
    def all_tags( self):
        """Return all the tags that are on any record."""
        return self.tags.keys()

    def tag_all( self, tag_string):
        """Apply a tag to each of the records."""
        for record in self:
            self.tag( record, tag_string)

    @classmethod
    def parse( cls, input_string):
        parse_result = read_taggable_collection( input_string)
        return cls( parse_result.data, tags=parse_result.tags)
