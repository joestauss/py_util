def select_from_list( input_list):
    """Prompts the user to select one or more from among a list of options.""" #v1
    explanation_prompt = "Enter the number for the selection(s) you would like, separated by a comma."
    print( explanation_prompt)

    valid_selections = []
    while not valid_selections:
        choices_prompt = "\n".join(
            [f'{i}:{" "*(4-len(str(i)))}{choice}' for i, choice in enumerate( input_list)]
            + [">>> "] )
        user_input = input( choices_prompt)

        print( f"User wants {user_input}.  This corresponds to the following selection(s):")
        selections = [s.strip() for s in user_input.split(",")]
        for selection in selections:
            try:
                valid_selections.append( input_list[ int(selection)])
                print(  "\t" + valid_selections[-1])
            except:
                print( "\t" + f"{selection} was not a valid choice.")
        if not valid_selections:
            print('There were no valid selections.  Please try again:\n' + explanation_prompt.upper())
    return valid_selections


def boxed_text( *args, BUFFER_SPACE=5 ):
    """boxed_text   is a function that pretty-prints its args in a box.

    Parameters
    -----------
        args
            Each arg in args will be interpretted as a string, unless it's a non-string iterable, in which case it will be unpacked.

        BUFFER_SPACE: int
            The number of spaces between the longest text line and the left/ right borders.
    """ #v1
    def unpack_strings( obj):
        if isinstance( obj, str) or not hasattr(obj, '__iter__'):
            return [ str (obj)]
        else:
            lines = []
            for item in obj:
                lines = lines + unpack_strings( item)
            return lines

    lines = unpack_strings( args)

    MAX_LEN         = max( map( lambda s: len(s), lines))
    GAP             = '||' + ' '*(MAX_LEN + 2*BUFFER_SPACE) +'||'
    HORIZONTAL_LINE = '='* (MAX_LEN + 2*BUFFER_SPACE + 4)
    RIGHT_BORDER    = '||' + ' '*BUFFER_SPACE
    LEFT_BORDER     =  ' '*BUFFER_SPACE + '||'
    TOP_BORDER      = (HORIZONTAL_LINE, GAP)
    BOTTOM_BORDER   = (GAP, HORIZONTAL_LINE)
    return "\n".join([*TOP_BORDER, *map( lambda l: RIGHT_BORDER + l + ' '*(MAX_LEN - len(l))+ LEFT_BORDER, lines), *BOTTOM_BORDER])
