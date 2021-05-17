import unittest
import pathlib
import json
import os
from py_util.data_structures import JSONDict, ReadOnlyJSONDict

_rsrc_dir = pathlib.Path( __file__).absolute().parents[1].joinpath( 'resources')

def next_temp_json_available():
    __base_dir = pathlib.Path( __file__).absolute().parent
    filename = 'temp.json'
    i = 0
    while filename in [f.name for f in list(__base_dir.glob('*.json'))]:
        filename = f'temp{i}.json'
        i += 1
    return filename

class Test_JSONDict( unittest.TestCase):
    __base_dir = pathlib.Path( __file__).parent
    def json_filenames():
        return [f.name for f in list(self.__base_dir.glob('*.json'))]

    def test_writing( self):
        filename = next_temp_json_available()
        test_file = _rsrc_dir.joinpath( filename)
        temp = JSONDict( test_file)
        temp[ 'A'] = 'a'
        temp[ 'B'] = 'b'
        temp[ 'C'] = 'c'
        temp[ 'C'] = 'ccc'
        del temp[ 'A']
        self.assertEqual( temp[ 'B'], 'b')
        self.assertEqual( temp[ 'C'], 'ccc')
        os.remove( test_file)

class Test_RO_JSONDict( unittest.TestCase):
    __base_dir = pathlib.Path( __file__).parent

    @property
    def json_filenames( self):
        return [f.name for f in list(self.__base_dir.glob('*.json'))]

    def test_fruits( self):
        test_file = _rsrc_dir.joinpath("fruits.json")
        print( test_file)
        self.assertTrue( test_file.exists())
        fruits = ReadOnlyJSONDict( test_file)
        self.assertEqual( fruits[ 'banana']    ,  'yellow')
        self.assertEqual( fruits[ 'strawberry'],  'red'   )
        self.assertEqual( fruits[ 'grapes']    ,  'purple')
        self.assertEqual( len( fruits), 3)

    def tesst_empty_file( self):
        filename = next_temp_json_available()
        test_file = self.__base_dir.joinpath( filename)
        self.assertTrue( filename not in self.json_filenames)
        empty_dict = ReadOnlyJSONDict( test_file)
        print( len(empty_dict))
        self.assertTrue( filename in self.json_filenames)
        os.remove( test_file)
