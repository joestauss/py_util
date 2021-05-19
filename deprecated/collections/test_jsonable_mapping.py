''' This module tests the JSONable mixin with a concrete class called JSONRecord.

JSONable Functionality tested
-----------------------------
    __eq__ and __repr__ --- Tested even though they are not implemented in JSONable as a check on inheriting from an abstract class.
    obj.json
    cls.from_json( json_string)
    __hash__
'''
import unittest
from py_util.collections import JSONableMapping, BaseMapping

class JSONRecord( BaseMapping, JSONableMapping):
    pass

class Test_JSONableMapping( unittest.TestCase):
    def setUp( self):
        self.dd_1   = {f'key {i}' : f'value {i}' for i in range(5)}
        self.dd_2   = {f'key {i}' : f'alternate value {i}' for i in range(5)}

        self.jr1     = JSONRecord( self.dd_1)
        self.jr2     = JSONRecord( self.dd_2)
        self.jrA     = JSONRecord( {"data":"AAA"})
        self.jrB     = JSONRecord( {"data":"BBB"})

        self.json_records = [ self.jr1, self.jr2, self.jrA, self.jrB]

    def test_JSONRecord_eq( self):
        self.assertEqual( self.jr1, JSONRecord( self.dd_1))
        self.assertEqual( self.jr2, JSONRecord( self.dd_2))
        self.assertTrue( self.jr1 != self.jr2)
        self.assertTrue( self.jrA != self.jrB)

    def test_JSONRecord_repr( self):
        for json_record in self.json_records:
            self.assertEqual( json_record, eval( repr( json_record)))

    def test_JSONRecord_json( self):
        for json_record in self.json_records:
            self.assertEqual( JSONRecord.from_json( json_record.json), json_record)

    def test_JSONRecord_hash( self):
        record_A1 = JSONRecord( {'A' : 'aaa'})
        record_A2 = JSONRecord( {'A' : 'aaa'})
        self.assertEqual( hash(record_A1), hash(record_A2))
        self.assertEqual( len( { record_A1, record_A2}), 1) 

if __name__ == "__main__":
    unittest.main()
