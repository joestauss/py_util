def spaced_strings( rows, as_table = False):
    num_rows = len( rows[0]) # It is assumed that all are the same length.

    longest = [ max( [ len( str( row[i])) for row in rows]) for i in range(num_rows) ]

    spaced_strings = []
    for i, row in enumerate( rows):
        spaced_strings.append([])
        for e, entry in enumerate( row):
            spaced_strings[i].append( str( entry) + (' ' * (longest[e] - len( str( entry)))))

    if as_table:
        return "\n".join( [" || ".join( row) for row in spaced_strings] )
    else:
        return spaced_strings
