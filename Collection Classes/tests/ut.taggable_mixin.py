"""This module tests Taggable class mixin.

Some of the base classes' functionality is tested also, to verify that everything works when inheriting from an abstract class.
"""

import unittest
from old_mixins import Taggable
from jsonable_mapping import JSONableMapping
from base_classes import BaseRecord, BaseCollection

class TaggableRecord(Taggable, BaseRecord, JSONableMapping):
    pass

class TaggableCollection( Taggable, BaseCollection):
    pass

class Test_TaggableClasses( unittest.TestCase):
    def setUp( self):
        dd_1   = {f'key {i}' : f'value {i}' for i in range(5)}
        tags_1 = { f'tag {i}' for i in range(3)}
        dd_2   = {f'key {i}' : f'alternate value {i}' for i in range(5)}
        tags_2 = { f'tag {i+1}' for i in range(3)}

        self.tr1     = TaggableRecord( dd_1, tags=tags_1)
        self.tr1_alt = TaggableRecord( dd_1, tags=tags_2)
        self.tr2     = TaggableRecord( dd_2, tags=tags_2)

        self.tds1    = TaggableCollection( {self.tr1, self.tr2})
        self.tds2    = TaggableCollection( {self.tr1_alt, self.tr2})

    def test_TaggableRecord_repr( self):
        self.assertEqual( self.tr1, eval( repr( self.tr1)))

    def test_TaggableRecord_eq( self):
        self.assertEqual( self.tr1, self.tr1_alt)
        self.assertTrue(  self.tr1 != self.tr2)

    def test_TaggableRecord_hash( self):
        self.assertEqual( hash( self.tr1), hash( self.tr1_alt))
        self.assertTrue(  hash( self.tr1) != hash( self.tr2))

    def test_TaggableRecord_tag( self):
        has_tags  = TaggableRecord( tags={'tag A', 'tag B'})
        gets_tags = TaggableRecord()
        gets_tags.tag( 'tag A')
        gets_tags.tag( 'tag B')
        self.assertEqual( has_tags.tags, gets_tags.tags )

    def test_TaggableCollection_eq( self):
        self.assertEqual( self.tds1, self.tds2)

    def test_TaggableCollection_repr( self):
        self.assertEqual( self.tds1, eval( repr( self.tds1)))

    def test_TaggableCollection_add( self):
        temp_tds = TaggableCollection()
        temp_tds.add( self.tr1)
        temp_tds.add( self.tr2)
        self.assertEqual(temp_tds, self.tds1)

        temp_tds = TaggableCollection( {TaggableRecord( tags={'A'})})
        temp_tds.add( TaggableRecord( tags={'B'}))
        self.assertEqual(TaggableCollection( {TaggableRecord( tags={'A', 'B'})}).tags, temp_tds.tags)

    def test_TaggableCollection_tag_all( self):
        self.tds2.tag_all( 'TEST TAG')
        for record in self.tds2.data:
            self.assertTrue( 'TEST TAG' in record.tags)

    def test_TaggableCollection_all_tags( self):
        self.assertEqual(
            TaggableCollection( {TaggableRecord( tags={'A', 'B'})}).all_tags,
            TaggableCollection( {TaggableRecord( tags={'A'}), TaggableRecord({'key':None}, tags={'B'})}).all_tags
         )

if __name__ == "__main__":
    unittest.main()
