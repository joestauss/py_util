""" The message_sandwich decorator prints a message before and after a function
call: not super useful, but I'm still figuring out the best way to implement a
decorator.
"""
import functools

class message_sandwich:
    def __init__( self, message="Default Message"):
        self.message = message

    def __call__( self, function):
        @functools.wraps( function)
        def decorated( *args, **kwargs):
            print( self.message)
            result = function( *args, **kwargs)
            print( self.message)
            return result
        return decorated


@message_sandwich( )
def print_args( *args, **kwargs):
    print( "\n".join(
        [f"\t{arg}" for arg in args] + [ f"\t{k}\t{v}" for k, v in kwargs.items()]
    ) )

if __name__ == "__main__":
    print_args( "hello")
