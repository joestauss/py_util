import unittest
from pyutil.classes.filtered_set import FilteredSet

class OddNumsSet( FilteredSet):
    def filter( self, item):
        return item % 2 == 1

class TestFilteredSet( unittest.TestCase):
    def test_oddnums_set( self):
        self.assertTrue( OddNumsSet( range(10)) == {1, 3, 5, 7, 9})

if __name__ == '__main__':
    unittest.main()
