import unittest
from py_util.data_structures import BaseSequence

class Test_BaseSequence( unittest.TestCase):
    ''' collections.abc.MutableSequence
        ===============================
            abstract methods
            ----------------
                __getitem__, __setitem__, __delitem__, __len__, insert

            mixin methods
            -------------
                from Sequence: __contains__, __iter__, __reversed__, index, count
                also: append, reverse, extend, pop, remove, __iadd__
    '''

    def test_BaseSequence_construction( self):
        temp = BaseSequence( [1, 2, 3])
        temp.reverse()
        self.assertEqual( temp.data, [3, 2, 1])
        temp.append( 4)
        self.assertEqual( temp.data, [3, 2, 1, 4])
        temp.pop( 1)
        self.assertEqual( temp.data, [3, 1, 4])
        temp += [1, 1]
        temp += BaseSequence([1, 1])
        self.assertEqual( temp.data, [3, 1, 4, 1, 1, 1, 1])
        self.assertEqual( temp.count( 1), 5)
        self.assertEqual( temp.index( 4), 2)
        self.assertEqual( temp[3:], [1] * 4)

if __name__ == "__main__":
    unittest.main()
