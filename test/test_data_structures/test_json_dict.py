import unittest
import pathlib
import json
from py_util.data_structures import ReadOnlyJSONDict

class Test_RO_JSONDict( unittest.TestCase):
    def test_fruits( self):
        test_file = pathlib.Path( __file__).parent.joinpath("fruits.json")
        fruits = ReadOnlyJSONDict( test_file)
        self.assertEqual( fruits[ 'banana']    ,  'yellow')
        self.assertEqual( fruits[ 'strawberry'],  'red'   )
        self.assertEqual( fruits[ 'grapes']    ,  'purple')
        self.assertEqual( len( fruits), 3)
