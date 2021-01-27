from sql_table import SQLTable
import collections

class BaseRecord( collections.UserDict):
    """A simple concrete record class for testing mixins.""" #v1
    def __init__( self, *args, **kwargs):
        super().__init__( *args, **kwargs)

    def __repr__( self):
        return f"{type(self).__name__}({repr( self.data)})"

    def __str__( self):
        return f"This is a {type(self).__name__} with {len( self.data)} items."

    def __hash__( self):
        return hash( repr( self))

class BaseCollection( collections.abc.MutableSet):
    """A simple concrete class representing a collection of records.  Used for testing micins.""" #v1
    def __init__( self, *args, **kwargs):
        self.data = set()
        if len(args) > 0:
            init_data = set(args[0])
            for record in init_data:
                self.add( record)
        if 'name' in kwargs:
            self.name = kwargs['name']
        else:
            self.name = "Nameless BaseCollection"

    def __repr__( self):
        return f"{type(self).__name__}({list( self.data)}, name={repr(self.name)})"

    def __str__( self):
        return f"This is a {type(self).__name__} with {len( self)} items."
    #
    #   Start of MutableSet methods
    #
    def __contains__(self, item):
        return item in self.data

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def add(self, item):
        if isinstance( item, BaseRecord):
            self.data.add(item)
        else:
            raise ValueError( "Tried to add a non-BaseRecord item to a BaseCollection.")

    def discard(self, item):
        self.data.pop(item)
    #
    #   End of MutableSet methods
    #

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
