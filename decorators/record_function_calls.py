# https://dev.to/mandrewcito/a-tiny-python-log-decorator-1o5m
# https://www.geeksforgeeks.org/create-an-exception-logging-decorator-in-python/


from py_util.decorators import LoggingDecorator
import functools
import time

class record_function_calls( LoggingDecorator):
    def __call__( self, function):
        @functools.wraps( function)
        def decorated( *args, **kwargs):
            result  = function( *args, **kwargs)
            now     = time.ctime( time.time())
            report  = f"{now}:{self.function_call_string( function, args, kwargs)}:::{str(result)}"
            self.logger.info( report)
            return result
        return decorated
