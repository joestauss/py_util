def cli_selector( input_list):
    def select_multiple( input_list):
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
    return select_multiple( input_list)
