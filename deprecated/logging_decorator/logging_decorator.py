import logging

def setup_logger( name):
    try:
        logger = logging.getLogger( name)
        logger.setLevel("DEBUG")
        formatter = logging.Formatter( '%(asctime)s :: %(levelname)s :: %(message)s')
        fh = logging.FileHandler(f"{name}.log")
        fh.setLevel( logging.INFO)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger
    except:
        raise ValueError( f"Unable to create logger with filepath: {filepath}")

class LoggingDecorator:
    logger = setup_logger( f"{__name__.split('.')[-1]}")

    @staticmethod
    def function_call_string( function, args, kwargs):
        name = function.__name__
        params = ', '.join( list( [str(a) for a in args]) + [ f"{k}={str(v)}" for k, v in kwargs.items()])
        return f"{name}( {params})"
