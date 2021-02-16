import re
import pyparsing as pp

def extract_dollar_amount( s):
    dollar_amounts = re.findall(r'\$[0-9,]+', s)
    try:
        return int(dollar_amounts[0][1:].replace(',', ''))
    except:
        return None

def extract_minute_amount( s):
    minute_amounts = re.findall(r'[0-9,]+ min', s)
    try:
        return int(minute_amounts[0][:-4].replace(',', ''))
    except:
        return None

def extract_film_identity( s):
    ''' extract_film_info is the swiss army knife of identifing films.

    Input
    -----
    s: str
        A single film to be identified.  Currently supported formats:
        - Title (Year)
        - Title (without a year)
        - IMDB film ID (can be anywhere, meaning this enables...)
        - a URL that contains an IMDB film ID

    Returns
    -------
    A tuple of (IMDB Film ID, title, year).
    If any of these are not in "s", None will be in its place.
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
