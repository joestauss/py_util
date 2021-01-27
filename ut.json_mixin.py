import unittest
import json
from json_mixin import JSONCollection, JSONRecord

class Test_JSONClasses( unittest.TestCase):
    def setUp( self):
        self.dd_1   = {f'key {i}' : f'value {i}' for i in range(5)}
        self.dd_2   = {f'key {i}' : f'alternate value {i}' for i in range(5)}

        self.jr1     = JSONRecord( data=self.dd_1)
        self.jr2     = JSONRecord( data=self.dd_2)
        self.jrA     = JSONRecord( data={"data":"AAA"})
        self.jrB     = JSONRecord( data={"data":"BBB"})

        self.jds1    = JSONCollection( data={self.jr1, self.jr2})
        self.jdsA    = JSONCollection( data={self.jrA})
        self.jdsB    = JSONCollection( data={self.jrB})
        self.jdsAB   = JSONCollection( data={self.jrA, self.jrB})

        self.json_records = [ self.jr1, self.jr2, self.jrA, self.jrB]


    def test_JSONRecord_eq( self):
        self.assertEqual( self.jr1, JSONRecord( data=self.dd_1))
        self.assertEqual( self.jr2, JSONRecord( data=self.dd_2))
        self.assertTrue( self.jr1 != self.jr2)
        self.assertTrue( self.jrA != self.jrB)

    def test_JSONRecord_repr( self):
        for json_record in self.json_records:
            self.assertEqual( json_record, eval( repr( json_record)))

    def test_JSONRecord_json( self):
        for json_record in self.json_records:
            self.assertEqual( JSONRecord.from_json( json_record.json), json_record)

    def test_JSONCollection_eq( self):
        self.assertEqual( self.jds1, JSONCollection( data={self.jr1, self.jr2}))

    def test_JSONCollection_repr( self):
        self.assertEqual( self.jds1, eval( repr( self.jds1)))

    def test_JSONCollection_add( self):
        temp_jds = JSONCollection()
        temp_jds.add( self.jr1)
        temp_jds.add( self.jr2)
        self.assertEqual(temp_jds, self.jds1)

    def test_JSONCollection_or( self):
        self.assertEqual( self.jdsAB, self.jdsA | self.jdsB)

if __name__ == "__main__":
    unittest.main()
