import collections.abc
from py_util.classes import BaseCollection

class BaseSequence( collections.abc.MutableSequence, BaseCollection):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        try:
            self.data = list( self.data)
        except:
            raise ValueError( "BaseSequence must be initialized with something that can be interpreted as an list.")

    #   Start of BaseSequence methods
    #   __len__ is implemented in BaseCollection.
    #
    def __setitem__(self, index, value):
        self.data[index] = value

    def __getitem__(self, index):
        return self.data[index]

    def __delitem__(self, index):
        del self.data[index]

    def insert(self, index, value):
        self.data.insert(index, value)
    #
    #   End of BaseSequence methods
