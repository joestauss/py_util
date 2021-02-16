import unittest
from py_util.collections import BaseMapping

class Test_BaseMapping( unittest.TestCase):
    ''' collections.abc.MutableMapping
        ==============================
            abstract methods
            ----------------
                __getitem__, __setitem__, __delitem__, __iter__, __len__

            mixin methods
            -------------
                from Mapping: __contains__, __eq__, __ne__,
                              keys, items, values, get
                also: pop, popitem, clear, update, setdefault
    '''

    def setUp( self):
        self.dd_1     = {f'key {i}' : f'value {i}' for i in range(5)}
        self.dd_1_alt = {f'key {i}' : f'alt. {i}'  for i in range(5)}
        self.dd_2     = {f'key {i}' : f'value {i}' for i in range(5)}

        self.mapping_1     = BaseMapping( self.dd_1)
        self.mapping_1_alt = BaseMapping( self.dd_1_alt)
        self.mapping_2     = BaseMapping( self.dd_2)
        self.mapping_A     = BaseMapping( {"aaa":"AAA"})
        self.mapping_B     = BaseMapping( {"bbb":"BBB"})
        self.mapping_AB    = BaseMapping( {"aaa":"AAA", "bbb":"BBB"})

        self.all_mappings = [
            self.mapping_1,
            self.mapping_2,
            self.mapping_A,
            self.mapping_B,
            self.mapping_AB
        ]

    def test_BaseMapping_repr( self):
        for mapping in self.all_mappings:
            self.assertEqual( mapping, eval( repr( mapping)))

    def test_BaseMapping_construction( self):
        temp = BaseMapping()
        temp['aaa'] = 'AAA'
        self.assertEqual( temp, self.mapping_A)
        del temp['aaa']
        self.assertEqual( temp.data, {})

    def test_BaseMapping_len( self):
        self.assertEqual( len( self.mapping_AB), 2)
        self.assertEqual( len( self.mapping_1),  5)

    def test_BaseMapping_kvi( self):
        self.assertEqual( self.mapping_1.keys(), self.mapping_1_alt.keys(), )
        self.assertEqual(
            set(self.mapping_AB.values()),
            set(self.mapping_A.values()) | set(self.mapping_B.values() ))
        self.assertEqual(
            dict(self.mapping_AB.items()),
            dict(self.mapping_A.items()) | dict(self.mapping_B.items() ))

if __name__ == "__main__":
    unittest.main()
