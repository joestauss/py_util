import functools
import time
from py_util.decorators import LoggingDecorator

class time_this (LoggingDecorator):
    def __call__( self, function):
        @functools.wraps( function)
        def decorated( *args, **kwargs):
            start   = time.time()
            result  = function( *args, **kwargs)
            end     = time.time()
            elapsed = end - start
            now     = time.ctime( time.time())
            report  = f"{now}:{self.function_call_string( function, args, kwargs)}:::{elapsed} seconds"
            self.logger.info( report)
            return result
        return decorated
