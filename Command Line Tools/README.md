# boxed\_text

__boxed_text__ is a pretty print function that puts its args in a box.

# cli\_selector( option\_list, mode='single', page_size = 10)

__cli_selector__ gets a user's input from among a list of options.  It should support three modes of operation:

* _single_ - User selects a single option.  This is the default mode.
* _many_ - User can select several options separated by a comma.
* _paginated_ - Options are presented in pages, which can be navigated between with '<' and '>'.  The *page_size* keyword is only significant in _paginated_ mode.

# MenuLoop

 __MenuLoop__ is a framework a "Select one of the following..."-type interface.
