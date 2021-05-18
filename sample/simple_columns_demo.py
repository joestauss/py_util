from py_util.text import simple_columns

test_data = [
    ("This is a really long line !!!!!!!!!!!!!", "first", "A", 1234),
    ("This is a shorter line.", "second", "A", 4321),
    ("", "third", "A", 0),
    ("This is the last line.", "fourth", "F", 232384073249839217480)
]

print( simple_columns( test_data, as_table=True))
