"""ut.common_repr.py

This script validates the performance of the @common_repr decorator.
It works by testing the __repr__ of decorated classes with different __init__ proiles.
"""
from py_util.decorators import common_repr
import unittest

class WrongRepr:
    def __init__( self, *args, **kwargs):
        pass

    def __repr__( self):
        return "This is not the correct REPR value for @common_repr."

    def __eq__( self, other):
        return self.__dict__ == other.__dict__

@common_repr
class EmptyInit( WrongRepr):
    def __init__( self, *args, **kwargs):
        super().__init__(*args, **kwargs)

@common_repr
class TwoArgs( WrongRepr):
    def __init__( self, a, b, *args, **kwargs):
        self.the_first_one = a
        self.numero_dos    = b
        super().__init__(*args, **kwargs)

    @property
    def _repr_args( self):
        return [ repr( self.the_first_one), repr( self.numero_dos)]

@common_repr
class ThreeKwargs( WrongRepr):
    def __init__(self, *args, alpha='A', gamma=3, **kwargs):
        self.alpha = alpha
        if 'beta' in kwargs:
            self.beta  = kwargs['beta']
        self.gamma = gamma
        super().__init__(*args, **kwargs)

    @property
    def _repr_kwargs( self):
        if not hasattr( self, 'beta'):
            return {'alpha' : self.alpha, 'gamma' : self.gamma}
        return {'alpha' : self.alpha, 'beta' : self.beta, 'gamma' : self.gamma}

class ComplexInit( TwoArgs, ThreeKwargs):
    def __init__( self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Test_CommonRepr( unittest.TestCase):

    def test_empty_call( self):
        object = EmptyInit()
        self.assertEqual( object, eval( repr( object)))

    def test_args_only( self):
        object = TwoArgs('Number One!!!', 2)
        self.assertEqual( object, eval( repr( object)))

    def test_kwargs_only( self):
        object = ThreeKwargs()
        self.assertEqual( object, eval( repr( object)))
        object.alpha = "Changed Value!"
        self.assertEqual( object, eval( repr( object)))

    def test_args_and_kwargs( self):
        object = ComplexInit( 'This is arg A.', 'This is arg B.', alpha='1234', beta={'beta':None}, gamma=None)
        self.assertEqual( object, eval( repr( object)))

if __name__ == '__main__':
    unittest.main()
