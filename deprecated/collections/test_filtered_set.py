import unittest
from py_util.collections import FilteredSet, BaseSet

class OddNumsSet( FilteredSet, BaseSet):
    def filter( self, item):
        return item % 2 == 1

class Test_FilteredSet( unittest.TestCase):
    def test_oddnums_set( self):
        self.assertTrue( OddNumsSet( range(10)) == {1, 3, 5, 7, 9})

if __name__ == '__main__':
    unittest.main()
