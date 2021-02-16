"""This module tests TaggableCollection mixin.

Some of the base class' functionality is tested also, to verify that everything works when inheriting from an abstract class.
"""

import unittest
from py_util.collections import TaggableCollection, BaseSequence

class TaggableRange( TaggableCollection, BaseSequence):
    def __init__( self, *args, **kwargs):
        if len( args) == 1:
            if isinstance( args[0], int):
                super().__init__( list( range( args[0])), **kwargs)
            elif isinstance( args[0], list):
                super().__init__( *args, **kwargs)
            else:
                raise ValueError( f"TaggableRange cannot be initialized with {args[0] =}")
        else:
            raise ValueError( "TaggableRange is initialized with a single parameter.")

class Test_TaggableCollection( unittest.TestCase):
    def setUp( self):
        self.all_taggables =     [
            TaggableRange( 4),
            TaggableRange( 4, name="I am four."),
            TaggableRange( 4, name="Odd numbers tagged!", tags={'Odd':{1, 3}})
        ]

    def test_Taggable_repr( self):
        for taggable in self.all_taggables:
            self.assertEqual( taggable.data, eval( repr( taggable)).data)
            self.assertEqual( taggable.name, eval( repr( taggable)).name)

    def test_TaggableSequence_tag( self):
        temp = TaggableRange( 11)
        temp.tag( 1, 'A')
        temp.tag( 2, 'A')
        temp.tag( 3, 'A')
        self.assertEqual( temp.tags, { 'A' : {1, 2, 3}})
        # also testing tag_all and discarding
        temp2 = TaggableRange( 4)
        temp2.tag_all( 'A')
        temp2.tags['A'].discard( 0)
        self.assertEqual( temp.tags, temp2.tags)

    def test_TaggableSequence_tagall( self):
        temp = TaggableRange( 15)
        temp.tag_all( 'Number')
        self.assertEqual( temp.tags, { 'Number' : set( range( 15))})
        # also testing tags in constructor
        temp2 = TaggableRange( 30, tags={ 'Number' : {i for i in range(15)}})
        self.assertEqual( temp.tags, temp2.tags)

    def test_TaggableSequence_all_tags( self):
        temp = TaggableRange( 3)
        temp.tag( 1, 'A')
        temp.tag( 1, 'B')
        temp.tag( 1, 'C')
        temp.tag( 2, 'A')
        temp.tag( 3, 'A')
        self.assertEqual( temp.all_tags, { 'A', 'B', 'C'})
        self.assertEqual( temp.tags, { 'A' : {1, 2, 3}, 'B' : {1}, 'C' : {1}})
        # also testing tags in the constructor
        temp2 = TaggableRange( 30, tags={ 'A' : {1, 2, 3}, 'B' : {1}, 'C' : {1}})
        self.assertEqual( temp.tags, temp2.tags)

if __name__ == "__main__":
    unittest.main()
