import unittest
from test_resources import *
from sql_table import *

class TestSQLTable( unittest.TestCase):
    def test_SQLTable_parser( self):
        for input, expected_output in TestCases.TableParser.validated_correct:
            self.assertEqual( SQLTable.parse( input), expected_output)

    def test_SQLTable_repr( self):
        for table_str in TestCases.TableClass.misc_tables:
            table1 = SQLTable.parse( table_str)
            table2 = eval( repr( table1))
            self.assertEqual(table1, table2)

    def test_SQLTable_normalization( self):
        for known_case in TestCases.TableClass.validated_normalizations:
            base_table = SQLTable.parse(known_case['base_table'])
            terminal_table = base_table.normalize_column('col2', 'col3')
            self.assertEqual( terminal_table, SQLTable.parse(known_case['expected_terminal_table']))
            self.assertEqual( base_table, SQLTable.parse(known_case['expected_connecting_table']))

    def test_SQLTable_add_pk( self):
        for input, expected_output in TestCases.TableClass.validated_pk_additions:
            working_table = SQLTable.parse( input)
            working_table.add_primary_key( 'pk')
            self.assertEqual( SQLTable.parse(expected_output), working_table)

    def test_SQLTable_text_field( self):
        for input, expected_output in TestCases.TextField.validated_length_25:
            self.assertEqual( expected_output, SQLTable._text_field( input, 25))

if __name__ == '__main__':
    unittest.main()
