import unittest
from nested_collection import NestedSequence

class TestNestedSequence( unittest.TestCase):
    def setUp( self):
        self.cases = [
        ('''
            No structure.
            No structure here.
            Just a flat group.
        ''', NestedSequence( ungrouped=[ 'No structure here.', 'No structure.', 'Just a flat group.'])),
        ('''
            Words in Spanish : {
                Uno
                Dos
                Tres
            }
            Words in English : {
                One; Two ;Three
            }
        ''', NestedSequence( groups={ 'Words in English' : ['Three', 'One', 'Two' ],
                                        'Words in Spanish' : ['Tres', 'Dos' , 'Uno' ],})),
        ('''
            Outer Group : {
                Inner Group : {
                    Thing
                }
            }
        ''', NestedSequence( groups={'Outer Group' : ['Thing'], 'Inner Group' : ['Thing']})),
        ('''
            Al Green
            Colors:{
                Primary Colors : {
                    Red
                    Yellow
                }
                Secondary Colors : {
                    Purple
                }
                    Black; Grey; White
                }
            The Blues
        ''', NestedSequence( subs={'Colors' : ['Yellow', 'Black', 'Purple', 'Red', 'Grey', 'White'],
                                       'Primary Colors' : ['Red', 'Yellow'],
                                       'Secondary Colors' : ['Purple']},
                            ungrouped=['The Blues', 'Al Green']))
        ]

    def test_parser( self):
        for input, expected_output in self.cases:
            self.assertEqual( NestedSequence.parse( input), expected_output)

    def test_repr( self):
        for input, expected_output in self.cases:
            # Both versions of cases are tested against eah other's repr to make sure order doesn't matter.
            self.assertEqual( eval( repr( NestedSequence.parse( input))), expected_output)
            self.assertEqual( eval( repr( NestedSequence.parse( input))), NestedSequence.parse( input))
            self.assertEqual( eval( repr( expected_output)), expected_output)
            self.assertEqual( eval( repr( expected_output)), NestedSequence.parse( input))

if __name__ == '__main__':
    unittest.main()
