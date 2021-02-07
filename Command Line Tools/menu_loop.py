from boxed_text   import boxed_text
from cli_selector import cli_selector

class MenuLoop:
    """MenuLoop is a framework for a basic, repeating CLI menu.

SubClasses should override, at minimum, the action_options property to add the
desired functionality. All implementations should leave the exit action/ option.
    """
    def __init__( self, *args, **kwargs):
        """Run the main loop.

Subclasses can load their parameters and then call MenuLoop's init to start.
        """
        self.exit_status = False
        while not self.exit_status:
            self.main_loop()

    def main_loop( self):
        """Read user's selection into a local variable, then execute it."""
        print( "Please select one of the following actions.")
        self.selection = cli_selector( list( self.action_options))
        self.action_options[ self.selection]()

    @property
    def action_options( self):
        """ The action_options parameter returns a dictionary:
            <OPTION TEXT> : <OPTION ACTION>
        Option Actions should be implemented as functions in the namespace of
        this method.
        """
        def exit():
            self.exit_status = True
        def nop():
            print( "You have selected: " + self.selection)
        return {
            "Do something."      : nop ,
            "Do something else." : nop ,
            "Exit."              : exit #exit should be in every main loop.
        }
