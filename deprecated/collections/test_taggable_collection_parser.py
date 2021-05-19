import unittest
from py_util.collections import TaggableCollection, BaseSet, BaseSequence
from collections     import namedtuple

class TaggableSet( TaggableCollection, BaseSet):
    @property
    def _repr_kwargs( self):
        return { 'tags': self.tags}

    def __eq__( self, other):
        return self.data == other.data and self.tags == other.tags

class TaggableSequence( TaggableCollection, BaseSequence):
    @property
    def _repr_kwargs( self):
        return { 'tags': self.tags}

    def __eq__( self, other):
        return self.data == other.data and self.tags == other.tags


ValidParse = namedtuple( 'ValidParse', 'input_text data tags')

class Test_TaggableCollection_parser( unittest.TestCase):
    def setUp( self):
        self.cases = [
            ValidParse('''
                No structure.
                No structure here.
                Just a flat group.
                ''',
                [ 'No structure.', 'No structure here.', 'Just a flat group.'],
                {}) ,
            ValidParse('''
                Words in Spanish : {
                    Uno
                    Dos
                    Tres
                }
                Words in English : {
                    One; Two ;Three
                }
                ''',
                [ 'Uno', 'Dos', 'Tres', 'One', 'Two', 'Three'],
                { 'Words in English' : ['One', 'Two', 'Three'],
                  'Words in Spanish' : ['Uno', 'Dos', 'Tres' ]}),
             ValidParse('''
                Outer Group : {
                    Inner Group : {
                        Thing
                    }
                }
                ''', ['Thing'],
                {'Outer Group' : ['Thing'], 'Inner Group' : ['Thing']}),
            ValidParse('''
                Al Green
                Colors:{
                    Primary Colors : {
                        Red
                        Yellow
                    }
                    Secondary Colors : {
                        Purple
                    }
                        Black; Grey; White; White
                    }
                The Blues
                ''',
                [ 'Al Green', 'Red', 'Yellow', 'Purple', 'Black', 'Grey', 'White', 'White', 'The Blues'],
                {'Colors' : ['Red', 'Yellow', 'Purple', 'Black', 'Grey', 'White', 'White'],
                 'Primary Colors' : ['Red', 'Yellow'],
                 'Secondary Colors' : ['Purple']})
            ]

    def test_parser( self):
        for case in self.cases:
            expected_sequence = TaggableSequence( case.data, tags=case.tags)
            expected_set      = TaggableSet(      case.data, tags=case.tags)

            self.assertEqual( TaggableSequence.parse( case.input_text), expected_sequence)
            self.assertEqual( TaggableSet.parse(      case.input_text), expected_set)

    def test_repr( self):
        for case in self.cases:
            parsed_sequence   = TaggableSequence.parse( case.input_text)
            parsed_set        = TaggableSet.parse(      case.input_text)
            expected_sequence = TaggableSequence( case.data, tags=case.tags)
            expected_set      = TaggableSet(      case.data, tags=case.tags)

            self.assertEqual( eval( repr( parsed_sequence  )), parsed_sequence)
            self.assertEqual( eval( repr( parsed_sequence  )), expected_sequence)
            self.assertEqual( eval( repr( expected_sequence)), parsed_sequence)
            self.assertEqual( eval( repr( expected_sequence)), expected_sequence)

            self.assertEqual( eval( repr( parsed_set  )), parsed_set)
            self.assertEqual( eval( repr( parsed_set  )), expected_set)
            self.assertEqual( eval( repr( expected_set)), parsed_set)
            self.assertEqual( eval( repr( expected_set)), expected_set)

if __name__ == '__main__':
    unittest.main()
