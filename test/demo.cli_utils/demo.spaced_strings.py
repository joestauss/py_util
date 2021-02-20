from py_util.cli import spaced_strings

test_data = [
    ("This is a really long line !!!!!!!!!!!!!", "first", 1234),
    ("This is a shorter line.", "second", 4321),
    ("", "third", 0),
    ("This is the last line.", "fourth", 232384073249839217480)
]

print( spaced_strings( test_data, as_table=True))
