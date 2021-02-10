import pyparsing as pp
pp.ParserElement.setDefaultWhitespaceChars(' \t')

class NestedCollection:
    ''' The NestedCollection class was implemented to provide access to the parser.

    Dunder Methods
    --------------
        __init__
        __eq__
        __repr__

    Other Methods
    -------------
        parse
    ''' #v1
    def __init__( self, ungrouped=[], groups={}):
        self.ungrouped = ungrouped
        self.groups    = groups

    def __eq__( self, other):
        for g, items in self.groups.items():
            if g not in other.groups:
                return False
            for item in items:
                if item not in other.groups[g]:
                    return False
        return sorted(self.ungrouped) == sorted( other.ungrouped)

    def __repr__( self):
        return f"NestedCollection(ungrouped={repr(self.ungrouped)}, groups={repr(self.groups)})"

    def parse( input_string):
        ''' Return a NestedCollection defined by input_string.

        Grammar
        -------
        * A collection consists of one or more groups and items.
        * An item is defined by its name.
        * A name cannot include the special characters ";:{}"
        * A group is written as
          <GROUP NAME> : {
            <COLLECTION>
          }
        * Whitespaces are significant!  Make sure that there is one after "{" and before "}".

        Grammar Example
        ---------------
        Loose item
        Outer group : {
            Inner group : {
                Stuff ; Stuff ; Stuff
            }
            In one group but not the other.
        }
        More loose items!
        '''
        BLANK_LINES   = pp.Suppress(pp.ZeroOrMore(pp.LineEnd()))
        END_ENTRY     = pp.Suppress(pp.Literal(";") | pp.Literal(":") |  pp.StringEnd() | pp.LineEnd())
        NAME          = pp.Combine( pp.OneOrMore( pp.Word( pp.printables, excludeChars=';:{}\n')), adjacent=False, joinString=' ')
        ITEM          = (NAME + END_ENTRY)('items*')
        GROUP_OPEN    = NAME +  pp.Suppress(":") + pp.Suppress("{")
        GROUP_CLOSE   = pp.Suppress( "}") + END_ENTRY
        COLLECTION    = pp.Forward()
        GROUP         = (GROUP_OPEN + BLANK_LINES + COLLECTION + GROUP_CLOSE)('groups*')
        COLLECTION    << pp.OneOrMore( GROUP | ITEM)
        DOC_STRUCTURE = BLANK_LINES + COLLECTION + BLANK_LINES

        NAME.setWhitespaceChars(' \t')
        result = DOC_STRUCTURE.parseString( input_string)
        g_names = []
        groups = {}
        if 'groups' in result:
            for group in result['groups']:
                g_names.append( group[0])
                groups[ group[0]] = list(filter( lambda item: item not in g_names, group))
        ungrouped = list(filter( lambda item: all(item not in g for g in groups.values() ), map( lambda item: item[0], result['items'].asList())))
        return NestedCollection(ungrouped=ungrouped, groups=groups)
