import collections.abc

class FilteredSet( collections.abc.MutableSet):
    def __contains__(self, item):
        return item in self.data

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def add(self, item):
        if self._filter( item):
            self.data.add(item)

    def discard(self, item):
        self.data.pop(item)

    def filter( self, item):
        return True
