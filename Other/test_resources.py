from sql_table import SQLTable
import collections

class TestCases:
    class TableParser:
        validated_correct = [(
        '''
        | col_1 | col_2 |
        | a     | b     |
        ''',
        SQLTable([{'col_1':'a', 'col_2': 'b'}])),
        ('''| col |
        | 1 |
        | 2 |''',
        SQLTable([{'col':i} for i in [1, 2]])
        )]

    class TableClass:
        validated_normalizations = [{
        'base_table' : '''
        | col1 | col2 |
        | a1   | A    |
        | b    | B    |
        | a2   | A    |''',
        'expected_terminal_table': '''
        | col2 | col3 |
        | A    | 0    |
        | B    | 1    |''',
        'expected_connecting_table': '''
        | col1 | col3 |
        | a1   | 0    |
        | b    | 1    |
        | a2   | 0    |''' }]

        misc_tables = [ '''
        | col_0 | col_1 | col_2 |
        | 0     | 1     | 2     |
        | Blah  | Blah  | Blah  |
        ''', '''
        | Alphas | Nums |
        | AAAAAA | 1234 |
        | BBBBBB | 5678 |
        | CCCCCC | 9900 |
        '''
        ]

        validated_pk_additions = [
        ('''
        | col |
        | A   |
        ''','''
        | pk | col |
        | 0  | A   |
        '''),('''
        | col_0 | col_1 | col_2 |
        | 0     | 1     | 2     |
        | Blah  | Blah  | Blah  |
        ''','''
        | pk | col_0 | col_1 | col_2 |
        | 0  | 0     | 1     | 2     |
        | 1  | Blah  | Blah  | Blah  |
        ''')
        ]

    class TextField:
        validated_length_25 = [
            ('12345678901234567890',
             '12345678901234567890'),
            ('123456789012345678901234567890',
             '1234567890123456789012...')
        ]
