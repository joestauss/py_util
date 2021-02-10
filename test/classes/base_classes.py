"""This module tests the BaseRecord and BaseCollection classes that I use to evaluate mixins.

BaseRecord Functionality Tested
-------------------------------
    __eq__
    __repr__
    Adding data with "record[ key] = value" syntax.
    __hash__ is tested by testing BaseCollection.add( base_record).

BaseCollection Functionality Tested
-----------------------------------
    __eq__
    __repr__
    .add( base_record) --- Including that it preserves uniqueness.
    Combining BaseCollection isntances with |.

"""
import unittest
from pyutil.classes.base_classes import BaseRecord, BaseCollection

class Test_BaseClasses( unittest.TestCase):
    def setUp( self):
        self.dd_1   = {f'key {i}' : f'value {i}' for i in range(5)}
        self.dd_2   = {f'key {i}' : f'alternate value {i}' for i in range(5)}

        self.record_1     = BaseRecord( self.dd_1)
        self.record_2     = BaseRecord( self.dd_2)
        self.record_A     = BaseRecord( {"data":"AAA"})
        self.record_B     = BaseRecord( {"data":"BBB"})

        # Collections are initialized with sets or lists; it shouldn't matter.
        self.collection_1    = BaseCollection( {self.record_1, self.record_2})
        self.also_collection_1 = BaseCollection( [self.record_1, self.record_2])
        self.collection_2    = BaseCollection( {self.record_1, self.record_A})
        self.collection_A    = BaseCollection( {self.record_A} )
        self.collection_B    = BaseCollection( [self.record_B])
        self.collection_AB   = BaseCollection( {self.record_A, self.record_B} )

        self.records     = [ self.record_1    , self.record_2    , self.record_A    , self.record_B]
        self.collections = [ self.collection_1, self.collection_2, self.collection_A, self.collection_B, self.collection_AB]

    def test_BaseRecord_eq( self):
        self.assertEqual( self.record_1, BaseRecord( self.dd_1))
        self.assertEqual( self.record_2, BaseRecord( self.dd_2))
        self.assertTrue( self.record_1 != self.record_2)
        self.assertTrue( self.record_A != self.record_B)

    def test_BaseRecord_repr( self):
        for Base_record in self.records:
            self.assertEqual( Base_record, eval( repr( Base_record)))

    def test_BaseRecord_add( self):
        temp_record = BaseRecord()
        temp_record['KEY'] = 'VALUE'
        self.assertEqual(temp_record, BaseRecord( {'KEY':'VALUE'}))

    def test_BaseCollection_eq( self):
        self.assertEqual( self.collection_1, self.also_collection_1)

    def test_BaseCollection_repr( self):
        self.assertEqual( self.collection_1, eval( repr( self.collection_1)))

    def test_BaseCollection_add( self):
        temp_collection_ = BaseCollection()
        temp_collection_.add( self.record_1)
        temp_collection_.add( self.record_2)
        temp_collection_.add( self.record_2)
        self.assertEqual(temp_collection_, self.collection_1)

    def test_BaseCollection_or( self):
        self.assertEqual( self.collection_AB, self.collection_A | self.collection_B)

if __name__ == "__main__":
    unittest.main()
