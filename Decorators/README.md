# Common Repr

The **\@common\_repr** decorator adds a representation of the typical form "ClassName( args, kwargs)".  It requires that the decorated class have two properties: args (a list) and kwargs (a dict).  Both should consist only of strings.

# Function Logger

Logs the time that a function was called, its parameters, and the return values to a file.

# Function Memoization

Caches the result of a function call.  If the closure has been evaluated before, the result will be delivered from the cache.

# Function Timer

Logs the time that a function takes to run (along with its parameters) to a file.
