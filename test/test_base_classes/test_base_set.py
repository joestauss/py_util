import unittest
from py_util.data_structures import BaseSet

class Test_BaseSet( unittest.TestCase):
    ''' collections.abc.MutableSet
        ==========================
            abstract methods
            ----------------
                __contains__, __iter__, __len__, add, discard

            mixin methods
            -------------
                from Set: __le__, __lt__, __eq__, __ne__, __gt__, __ge__,
                          __and__, __or__, __sub__, __xor__, isdisjoint
                also: clear, pop, remove, __ior__, __iand__, __ixor__, __isub__
    '''

    def test_BaseSet_construction( self):
        temp = BaseSet()
        self.assertEqual( len( temp), 0)
        temp.add( 'A')
        self.assertEqual( len( temp), 1)
        temp.add( 'B')
        self.assertEqual( len( temp), 2)
        temp.add( 'A')
        self.assertEqual( len( temp), 2)
        self.assertTrue( temp >= {'A'})
        temp.clear()
        self.assertEqual( len( temp), 0)

if __name__ == "__main__":
    unittest.main()
