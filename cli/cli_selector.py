def cli_selector( option_list, mode='single'):
    """Prompts the user to select from a list of options.

    Supports two modes of operation:
        -   'single'   : select a single option.
        -   'multiple' : can select several options, separated by a comma.
    """
    def select_single( option_list):
        """Prompts the user to select a single option from a list."""
        explanation_prompt = "Enter the number for your choice."
        choices_prompt = "\n".join(
            [f'{i}:{" "*(4-len(str(i)))}{option}' for i, option in enumerate( option_list)]
            + [">>> "] )
        failure_prompt = f"TRY AGAIN: Your input must be a single integer between 0 and {(len( option_list))-1}."

        print( explanation_prompt)
        while True:
            user_input = input( choices_prompt)
            try:
                return option_list[ int( user_input)]
            except:
                print( failure_prompt)

    def select_multiple( option_list):
        """Prompts the user to select one or more from among a list of options.""" #v1
        explanation_prompt = "Enter the number for your choice(s), separated by a comma."
        choices_prompt = "\n".join(
            [f'{i}:{" "*(4-len(str(i)))}{option}' for i, option in enumerate( option_list)]
            + [">>> "] )
        failure_prompt = 'There were no valid selections.  Please try again.'

        print( explanation_prompt)
        while True:
            valid_selections = []
            user_input = input( choices_prompt)
            selections = [s.strip() for s in user_input.split(",")]
            for selection in selections:
                try:
                    valid_selections.append( option_list[ int(selection)])
                except:
                    print( "\t" + f'"{selection}" was not a valid selection.')
            if valid_selections:
                return valid_selections
            print( failure_prompt)
            
    if mode == 'single':
        return select_single( option_list)
    elif mode == 'multiple':
        return select_multiple( option_list)
    else:
        raise ValueError( "CLI Selector can only be called in 'single' or 'many' modes.")
