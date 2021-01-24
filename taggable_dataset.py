import json

class TaggableRecord:
    """A TaggableRecord combines a data dictionary with a set of tags.

    Dunder Methods
    --------------
        __init__
        __repr__
        __hash__
        __str__
        __len__
        __eq__

    Properties
    -----------
        json
        dd

    Methods
    -------
        tag
    """ #v1
    def __init__( self, dd={}, tags=set()):
        self._data_dictionary = dd
        self.tags = set( tags) # set() so that a list/ whatever other iterable can be passed into __init__.

    def __repr__( self):
        return f"TaggableRecord( dd={repr(self._data_dictionary)}, tags={repr(self.tags)})"

    def __hash__( self):
        return hash('_'.join(map( lambda i: f"{i[0]}::{i[1]}", self.dd.items())))

    def __str__( self):
        return f"TaggableRecord containing {len( self)} items and {len( self.tags)} tags."

    def __len__( self):
        return len( self._data_dictionary)

    def __eq__( self, other):
        """TaggableRecord equality ignores tags, and only compares the data dictionaries."""
        return all( map(lambda item: (item in other._data_dictionary) and (other._data_dictionary[item] == self._data_dictionary[item]), self._data_dictionary))

    @property
    def dd( self):
        """Return the data dictionary for this TaggableRecord."""
        return self._data_dictionary

    @property
    def json( self):
        """Return a json representation of the data dictionary.  Tags are not saved."""
        return json.dumps( self._data_dictionary)

    def tag( self, tag):
        """Add the parameter to this TaggableRecord's "tags" set."""
        self.tags.add( tag)

class TaggableDataset:
    """A TaggableDataset encapsulates a (named) list of TaggableRecords.

    Initialization Parameters
    -------------------------
        data : Iterable( TaggableRecord)
            Will be stored as a set.

        name : str

    Dunder Methods
    --------------
        __init__
        __repr__
        __len__
        __str__
        __eq__

    Property Methods
    ----------------
        json
        tags

    Instance Methods
    ----------------
        tag_all
        add
    """#v1
    def __init__( self, data=set(), name='Taggable Dataset'):
        self.data = set()
        for record in data:
            self.add( record)
        self.name = name

    def __repr__( self):
        return f"TaggableDataset( data={repr( self.data)})"

    def __len__( self):
        return len( self.data)

    def __str__( self):
        return "\n".join([f"{self.name}\n{'='*len( self.name)}"] + map( lambda d: str(d), self.data) )

    def __eq__( self, other):
        return all( map( lambda d: d in other.data, self.data))

    @property
    def json( self):
        """Return a json representation of the TaggableRecords."""
        return json.dumps( {'name': self.name, 'data' : self.data})

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

    def add( self, taggable_record):
        """Add taggable_record to the data set.  If a record is found with the same data, the sets of tags are combined."""
        if taggable_record in self.data:
            print( 'Here')
            for record in self.data:
                if record == taggable_record:
                    record.tags = record.tags | taggable_record.tags
        self.data.add( taggable_record)

if __name__ == '__main__':
    help( TaggableDataset)
