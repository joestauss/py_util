import logging

class LoggingDecorator:
    logger = logging.getLogger( __name__)
    logger.setLevel( logging.INFO)
    logger.addHandler( logging.FileHandler( f"{__name__.split('.')[-1]}.log"))

    @staticmethod
    def function_call_string( function, args, kwargs):
        name = function.__name__
        params = ', '.join( list( [str(a) for a in args]) + [ f"{k}={str(v)}" for k, v in kwargs.items()])
        return f"{name}( {params})"
