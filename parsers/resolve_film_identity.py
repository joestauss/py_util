from collections import namedtuple

FilmIDResult = namedtuple( 'FilmIDResult', [ 'title', 'year', 'decade'])

def resolve_film_identity( s):
    '''
    resolve_film_identity is the swiss army knife of identifing films.  It is
    capable of determining both

    Grammar Rules
    -------------
        1.  Film identities are based on the title.
        2.  All words must be spelled correctly and all punctuation removed.
        3A. The year is any four digit number before or after the title.
        3B. Alternatively, a decade can be declared ( "70's" or "00s" etc.)
        4A. The title may be quoted (useful for films that CONTAIN a four digit
            number, such as "Cherry 2000", which came out in 1987), or not.
        4B. The year/ decade may be parenthesized, or not.

    Returns
    -------
    A namedtuple containing the (title, year, decade).
    If any of these are not in the input string, None will be in its place.
    '''
    YEAR_PAREN     = pp.Suppress("(") + pp.Word(pp.nums).setParseAction( lambda x: int(x[0]) ).setResultsName('year') + pp.Suppress(")")
    TITLE          = pp.OneOrMore( pp.Word(pp.printables, excludeChars='()')).setParseAction(lambda x: ' '.join(x)).setResultsName("title")
    TITLE_AND_YEAR = pp.Group(TITLE + pp.Optional(YEAR_PAREN)).setResultsName('Title and Year Pairs', listAllMatches=True)
    IMDB_FILM_ID   = pp.Regex("tt\d+")

    s = s.replace(u'\xa0', ' ')
    film_id = IMDB_FILM_ID.searchString(s)
    if film_id:
        return (film_id[0][0], None, None)
    result = TITLE_AND_YEAR.parseString(s)
    if len(result[0]) == 1:
        return (None, result[0][0], None)
    return ( None, result[0][0], result[0][1])
