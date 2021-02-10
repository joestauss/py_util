from py_util.cli import boxed_text

if __name__ == '__main__':
    print( boxed_text(  'This is a single parameter function call.'))
    # =======================================================
    # ||                                                   ||
    # ||     This is a single parameter function call.     ||
    # ||                                                   ||
    # =======================================================

    print( boxed_text([ 'Item 1 in List 1', 'Item 2 in List 1'],[ 'Item 1 in List 2', 'Item 2 in List 2']))
    # ==============================
    # ||                          ||
    # ||     Item 1 in List 1     ||
    # ||     Item 2 in List 1     ||
    # ||     Item 1 in List 2     ||
    # ||     Item 2 in List 2     ||
    # ||                          ||
    # ==============================

    print( boxed_text(  'This is the first parameter.', 'This is the second parameter.', 'This is the third parameter.'))
    # ===========================================
    # ||                                       ||
    # ||     This is the first parameter.      ||
    # ||     This is the second parameter.     ||
    # ||     This is the third parameter.      ||
    # ||                                       ||
    # ===========================================

    print( boxed_text(  'A string with a newline character has \n undefined behavior.'))
    # =========================================================================
    # ||                                                                     ||
    # ||     A string with a newline character has
    #  undefined behavior.     ||
    # ||                                                                     ||
    # =========================================================================
