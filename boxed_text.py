def boxed_text( *args, BUFFER_SPACE=5 ):
    """boxed_text   is a function that pretty-prints its args in a box.

Parameters
-----------
    args
        Each arg in args will be interpretted as a string, unless it's a non-string iterable, in which case it will be unpacked.

    BUFFER_SPACE: int
        The number of spaces between the longest text and the left/ right borders.

    """ #v1
    def unpack_strings( obj):
        if isinstance( obj, str) or not hasattr(obj, '__iter__'):
            return [ str (obj)]
        else:
            lines = []
            for item in obj:
                lines = lines + unpack_strings( item)
    lines = unpack_strings( args)

    MAX_LEN         = max( map( lambda s: len(s), lines))
    GAP             = '||' + ' '*(MAX_LEN + 2*BUFFER_SPACE) +'||'
    HORIZONTAL_LINE = '='* (MAX_LEN + 2*BUFFER_SPACE + 4)
    RIGHT_BORDER    = '||' + ' '*BUFFER_SPACE
    LEFT_BORDER     =  ' '*BUFFER_SPACE + '||'
    TOP_BORDER      = (HORIZONTAL_LINE, GAP)
    BOTTOM_BORDER   = (GAP, HORIZONTAL_LINE)
    return "\n".join([*TOP_BORDER, *map( lambda l: RIGHT_BORDER + l + ' '*(MAX_LEN - len(l))+ LEFT_BORDER, lines), *BOTTOM_BORDER])
