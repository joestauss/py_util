import unittest
from collections     import namedtuple
from py_util.parsers import extract_dollar_amount, \
                            extract_minute_amount, \
                            extract_film_identity

class Test_MinuteExtractor( unittest.TestCase):
    def setUp( self):
        TestCase = namedtuple( 'TestCase', 'input output')
        self.test_cases = [
            TestCase('123 min', 123),
            TestCase('\nblah45 minblahblah', 45),
            TestCase('67 minutes', 67),
            TestCase('89 min.', 89),
            TestCase('1011 seconds', None),
            TestCase('They talked for 1,213 minutes', 1213),
            TestCase('0 min', 0)
        ]

    def test_min_extractor( self):
        for case in self.test_cases:
            self.assertEqual( extract_minute_amount( case.input), case.output)

class Test_DollarExtractor( unittest.TestCase):
    def setUp( self):
        TestCase = namedtuple( 'TestCase', 'input output')
        self.test_cases = [
            TestCase('$123', 123),
            TestCase('\nblah$45 minblahblah', 45),
            TestCase('$67', 67),
            TestCase('$8,910', 8910),
            TestCase('11 dollars', None),
            TestCase('They did it for $1,213 dollars.', 1213),
            TestCase('$0', 0)
        ]

    def test_dollar_extractor( self):
        for case in self.test_cases:
            self.assertEqual( extract_dollar_amount( case.input), case.output)

class Test_FilmIdentityExtractor( unittest.TestCase):
    def setUp( self):
        TestCase = namedtuple( 'TestCase', 'input output')
        self.test_cases = [
            TestCase('tt2347386', ('tt2347386', None, None)), # a valid imdb id
            TestCase('Terminator (1492)', ( None, 'Terminator', 1492)), # a valid film-and-date.
            TestCase('I am the muffin man', (None, 'I am the muffin man', None)), # neither of the above, assumed to be a title.
            TestCase('Deltron(3030)', (None, 'Deltron', 3030)), # No space, should still work.
            TestCase('Beastmaster 2000 (1982)', (None, 'Beastmaster 2000', 1982)), # something like this started this whole fix
            TestCase('/embedded/link/tt234/j/', ('tt234', None, None)) # this should locate the film_id
        ]

    def test_film_id_extractor( self):
        for case in self.test_cases:
            self.assertEqual( extract_film_identity( case.input), case.output)

if __name__ == '__main__':
    unittest.main()
