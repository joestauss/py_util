"""The SQL Utility currently only contains the SQLTable class.

This class was originally used to facilitate a school project, and is not a
serious attempt to implement SQL.
"""
from utility import BaseSequence
import pyparsing as pp

class SQLTable( BaseSequence):
    """
SQLTable performs basic operations for relational data.  Rows are stored in a
list of dictionaries, which can be accessed by interacting with the SQLTable as
if it were a list or directly through the object.data attribute.

Instance Methods
----------------
    __eq__
    add_primary_key
    contains_row
    insert_all
    normalize_column

Static Methods
--------------
    insert_from_dd
    _text_field
    text_field_l
    text_field_m
    text_field_ls
    parse
    """
    def __eq__(self, other):
        """This __eq__ cannot be implemented at BaseSequence level becuse it doesn't care about row location."""
        return len(self) == len(other) and all( map( other.contains_row, self.data))

    def add_primary_key( self, primary_key_name):
        """ Add a primary key to the table.  The name of the primary key must be supplied, and its values are the integers 0 -- len( self.data). """
        self.data = [ { primary_key_name : i, **row} for i, row in enumerate( self.data)  ]

    def contains_row( self, search_row):
        """ Return True if this table contains search_row"""
        return any( map (lambda row: len(row) == len( [c for c in row if c in search_row and row[c] == search_row[c]]), self.data))

    def insert_all( self, target_table):
        """ Return a string containing INSERT INTO statements for every row in the table. """
        return "\n".join(  [SQLTable.insert_from_dd( target_table, row) for row in self.data])

    def normalize_column( self, normalization_column, connecting_column):
        """ Normalize a column of this table and return the newly-created terminal table.

        Parameters
        ----------
            normalization_column : str
                The name of the column that is to normalized by.

            connecting_column : str
                The name for the newly-created common column between the tables.

        Returns
        -------
            An SQLTable containing the unqiue values in normalization_column.
            This table will be modified to reflect the normalization procedure.
        """
        # Begin by finding the unique values in the normalization column, and using it to construct the terminal table.
        unique_norm_col_values = []
        for row in self.data:
            norm_col_value = row[ normalization_column]
            if norm_col_value not in unique_norm_col_values:
                unique_norm_col_values.append( norm_col_value)
        terminal_table = [ { connecting_column : i, normalization_column: value} for i, value in enumerate(unique_norm_col_values)]
        # Next use a lookup table to put new values in rows of the connecting table, and return the terminal table.
        lookup = { value: i for i, value in enumerate(unique_norm_col_values)}
        for row in self.data:
            row[ connecting_column] = lookup[ row[ normalization_column]]
            row.pop( normalization_column)
        return SQLTable( terminal_table)

    @staticmethod
    def insert_from_dd( table_name, dd):
        """ Create a statement to INSERT INTO table_name the row represented by the dd dictionary. """
        def transform_cell( c):
            if isinstance( c, str):
                return  f'"{c}"'
            elif c == None:
                return 'Null'
            return str( c)
        k_s = dd.keys()
        v_s = map(transform_cell, dd.values())
        return f'INSERT INTO {table_name} ({", ".join(k_s)}) VALUES ({", ".join(v_s)});'

    @staticmethod
    def _text_field(input_string, text_length):
        """Prepare a string to be loaded into a SQL table.
        1) Replace quotation marks with a single tic (').
        2) If len(input_string) > text_length, truncate with an ellipsis (...)."""
        if len(input_string) > text_length:
            input_string = input_string[:text_length-3] + '...'
        return input_string.replace( '"', "'")

    @staticmethod
    def text_field_l(s):
        """ See _text_field docstring."""
        return SQLTable._text_field(s, 400)

    @staticmethod
    def text_field_m(s):
        """ See _text_field docstring."""
        return SQLTable._text_field(s, 200)

    @staticmethod
    def text_field_s(s):
        """ See _text_field docstring."""
        return SQLTable._text_field(s, 45)

    @staticmethod
    def parse( table_string):
        """ Interprets markdown-style tables, with the first row as a header:
            | column 1 | column 2 | column 3|
            | a        | b        | c       |
            | 1        | 2        | 3       |
        Columns don't have to line up; all that matters is that each row is "|"-delimited.

        Parameters
        ----------
        table_string: string
          A string multi-line string of "|"-delimited rows.  There can be blank rows, but comments are not yet supported.

        Returns
        -------
        An SQLTable containing the same data as test_string.
        """

        INTEGER  = pp.Word(pp.nums).setParseAction(lambda x: int(x[0]))
        STRING   = pp.OneOrMore(pp.Word(pp.alphanums, pp.alphanums+'_'))
        CELL     = INTEGER | STRING
        ROW      = pp.Suppress("|") + pp.delimitedList(CELL, delim='|').setParseAction(lambda x: [x]) + pp.Suppress("|")
        ROW_LINE = ROW + pp.Suppress(pp.LineEnd())
        TABLE    = ROW_LINE.setResultsName("header") + pp.OneOrMore(ROW_LINE).setResultsName("data") + pp.StringEnd()

        result = TABLE.parseString( table_string)
        header = result.header[0]
        data   = result.data

        return SQLTable( [{header[i]: row[i] for i in range( len( header))} for row in data])
