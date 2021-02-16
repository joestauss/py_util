import pyparsing as pp
from collections import namedtuple

pp.ParserElement.setDefaultWhitespaceChars(' \t')
def read_taggable_collection( input_string):
    ''' Return a NestedSequence defined by input_string.

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
    ITEM_ENTRY    = (NAME + END_ENTRY)('items*')
    TAG_OPEN      = NAME +  pp.Suppress(":") + pp.Suppress("{")
    TAG_CLOSE     = pp.Suppress( "}") + END_ENTRY
    COLLECTION    = pp.Forward()
    TAG_ENTRY     = (TAG_OPEN + BLANK_LINES + COLLECTION + TAG_CLOSE)('tags*')
    COLLECTION    << pp.OneOrMore( TAG_ENTRY | ITEM_ENTRY)
    DOC_STRUCTURE = BLANK_LINES + COLLECTION + BLANK_LINES

    NAME.setWhitespaceChars(' \t')
    result = DOC_STRUCTURE.parseString( input_string)
    t_names = []
    tags = {}
    if 'tags' in result:
        for tag in result['tags']:
            tag_name = tag[ 0]
            t_names.append( tag_name)
            tags[ tag_name] = list( filter( lambda item: item not in t_names, tag))
    data =  [ item[ 0] for item in result['items'].asList()]

    ParseResult = namedtuple( 'ParseResult', [ 'data', 'tags'])
    return ParseResult( data, tags)









    #
    # nested_sequence.py
    #
    # from py_util.classes import BaseSequence, TaggableCollection
    # import pyparsing as pp
    #
    # pp.ParserElement.setDefaultWhitespaceChars(' \t')
    # class NestedSequence( TaggableCollection, BaseSequence):
    #     '''
    #     Methods
    #     -------
    #         __init__
    #         parse
    #     ''' #v1
    #     def __init__( self, *args, **kwargs):
    #         super().__init__(*args, **kwargs)
    #         self.groups = {}
    #         if 'tags' in kwargs:
    #             self.groups = kwargs[ 'subs']
    #
    #     @classmethod
    #     def parse( cls, input_string):
    #         ''' Return a NestedSequence defined by input_string.
    #
    #         Grammar
    #         -------
    #         * A collection consists of one or more groups and items.
    #         * An item is defined by its name.
    #         * A name cannot include the special characters ";:{}"
    #         * A group is written as
    #           <GROUP NAME> : {
    #             <COLLECTION>
    #           }
    #         * Whitespaces are significant!  Make sure that there is one after "{" and before "}".
    #
    #         Grammar Example
    #         ---------------
    #         Loose item
    #         Outer group : {
    #             Inner group : {
    #                 Stuff ; Stuff ; Stuff
    #             }
    #             In one group but not the other.
    #         }
    #         More loose items!
    #         '''
    #         BLANK_LINES   = pp.Suppress(pp.ZeroOrMore(pp.LineEnd()))
    #         END_ENTRY     = pp.Suppress(pp.Literal(";") | pp.Literal(":") |  pp.StringEnd() | pp.LineEnd())
    #         NAME          = pp.Combine( pp.OneOrMore( pp.Word( pp.printables, excludeChars=';:{}\n')), adjacent=False, joinString=' ')
    #         ITEM          = (NAME + END_ENTRY)('items*')
    #         GROUP_OPEN    = NAME +  pp.Suppress(":") + pp.Suppress("{")
    #         GROUP_CLOSE   = pp.Suppress( "}") + END_ENTRY
    #         COLLECTION    = pp.Forward()
    #         GROUP         = (GROUP_OPEN + BLANK_LINES + COLLECTION + GROUP_CLOSE)('groups*')
    #         COLLECTION    << pp.OneOrMore( GROUP | ITEM)
    #         DOC_STRUCTURE = BLANK_LINES + COLLECTION + BLANK_LINES
    #
    #         NAME.setWhitespaceChars(' \t')
    #         result = DOC_STRUCTURE.parseString( input_string)
    #         g_names = []
    #         groups = {}
    #         if 'groups' in result:
    #             for group in result['groups']:
    #                 g_names.append( group[0])
    #                 groups[ group[0]] = list(filter( lambda item: item not in g_names, group))
    #         ungrouped = list(filter( lambda item: all(item not in g for g in groups.values() ), map( lambda item: item[0], result['items'].asList())))
    #         return cls(ungrouped, subs=groups)
