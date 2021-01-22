# my-python-utilities

This repository contains various general-purpose python tools that I have developed.

# Compatibility, Use, and Versioning

In order to be able to refactor however and whenever I want, I will not be enforcing backwards compatibility on any of these utilities.  To use this code in another project, copy what is needed into a "utility.py" module in the other repository.  As better versions of these utilties are developed, I may want to update other projects' "utility.py" modules, so it will be important to know which version of each utility I'm using.  Versioning will be implemented with a short comment (#vN) after each docstring.

# Architecture

 Each function or class should be in a standalone module (so, for example, the "boxed\_text" function is not in a more-general "print\_utilities" module).  Resources for unit testing include "test_resources.py" and anything named ut.\_.py.
