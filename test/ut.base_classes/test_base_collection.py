import unittest
from py_util.classes import BaseCollection
from collections import namedtuple

class Test_BaseCollection( unittest.TestCase):
    ''' collections.abc.Collection
        ==========================
        *   abstract methods: __contains__, __iter__, and __len__
        *   There are no mixin methods for this class.
    '''

    def setUp( self):
        CollectionTestCase = namedtuple( 'CollectionTestCase', ['collection', 'true_length'])
        self.all_collections = [
            CollectionTestCase( BaseCollection(), 0),
            CollectionTestCase( BaseCollection( (1, 2, 3, 4), name="I am a tuple."), 4),
            CollectionTestCase( BaseCollection( [i**2 for i in range(30)], name="List"), 30),
            CollectionTestCase( BaseCollection( {'a' : 'A', 'b' : 'B'}, name="Mr. Dictionary"), 2) ]

    def test_BaseCollection( self):
        for collection, true_length in self.all_collections:
            self.assertEqual( collection.data, eval( repr( collection)).data)
            self.assertEqual( collection.name, eval( repr( collection)).name)
            self.assertEqual( len( collection),  true_length)

    def test_BaseCollection_contains( self):
        self.assertTrue( 'everything' not in self.all_collections[0].collection)
        self.assertTrue( 4 in self.all_collections[1].collection)
        self.assertTrue( 9 in self.all_collections[2].collection)
        self.assertTrue( 'a' in self.all_collections[3].collection)

if __name__ == "__main__":
    unittest.main()
