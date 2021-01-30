import unittest
from nested_collection import NestedCollection

class TestNestedCollection( unittest.TestCase):
    def setUp( self):
        self.cases = [
        ('''
            No structure.
            No structure here.
            Just a flat group.
        ''', NestedCollection( ungrouped=[ 'No structure here.', 'No structure.', 'Just a flat group.'])),
        ('''
            Words in Spanish : {
                Uno
                Dos
                Tres
            }
            Words in English : {
                One; Two ;Three
            }
        ''', NestedCollection( groups={ 'Words in English' : ['Three', 'One', 'Two' ],
                                        'Words in Spanish' : ['Tres', 'Dos' , 'Uno' ],})),
        ('''
            Outer Group : {
                Inner Group : {
                    Thing
                }
            }
        ''', NestedCollection( groups={'Outer Group' : ['Thing'], 'Inner Group' : ['Thing']})),
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
        ''', NestedCollection( groups={'Colors' : ['Yellow', 'Black', 'Purple', 'Red', 'Grey', 'White'],
                                       'Primary Colors' : ['Red', 'Yellow'],
                                       'Secondary Colors' : ['Purple']},
                            ungrouped=['The Blues', 'Al Green']))
        ]

    def test_parser( self):
        for input, expected_output in self.cases:
            self.assertEqual( NestedCollection.parse( input), expected_output)

    def test_repr( self):
        for input, expected_output in self.cases:
            # Both versions of cases are tested against eah other's repr to make sure order doesn't matter.
            self.assertEqual( eval( repr( NestedCollection.parse( input))), expected_output)
            self.assertEqual( eval( repr( NestedCollection.parse( input))), NestedCollection.parse( input))
            self.assertEqual( eval( repr( expected_output)), expected_output)
            self.assertEqual( eval( repr( expected_output)), NestedCollection.parse( input))

if __name__ == '__main__':
    unittest.main()
