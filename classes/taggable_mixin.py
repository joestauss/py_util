import collections.abc

class Taggable():
    """A Taggable object can can be given temporary tags, or be a container for Taggable objects.

    Methods for All Taggables
    -------------------------
        Taggable__init__ --- adds the "tags" attribute to the object.
        Taggable.tag( tag_string)

    Methods and Properties for Taggable Collections
    -----------------------------------------------
        Taggable.taggable_records
        Taggable.all_tags
        Taggable.tag_all( tag_string)
    """ #v
    def __init__( self, *args, tags=set(), **kwargs):
        """Add the tags attribute."""
        super().__init__(*args, **kwargs)
        self.tags = tags

    def tag( self, tag_string):
        """Add the parameter to this TaggableRecord's "tags" set."""
        self.tags.add( tag_string)

    @property
    def taggable_records( self):
        """Return any taggable objects, but raise an error if its not a collection."""
        if not isinstance( self, collections.abc.Collection):
            raise TypeError("The taggable_records property is only available for collections.")
        for record in self:
            if isinstance( record, Taggable):
                yield record

    @property
    def all_tags( self):
        """Return all the tags that are on any record."""
        all_tags = set()
        for record in self.taggable_records:
            all_tags = all_tags | record.tags
        return all_tags

    def tag_all( self, tag_string):
        """Apply a tag to each of the records."""
        for record in self.taggable_records:
            record.tag( tag_string)
