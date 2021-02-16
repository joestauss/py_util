# py-util

This repository contains various general-purpose python tools that I use.  This repo will work as a package as long as it's in your Python path.



# py_util.cli

**cli** contains any command-line tools that I have.  This includes cookie-cutter pretty-print functions.

* __boxed\_text__ is a pretty-print function that puts its args in a box made of #.  Any iterables are unpacked and everything is given its own line with a customizable-width buffer of space.

* __cli\_selector__ gets a user's input from among a list of options.  It supports two modes of operation, _single_ and _many_.

* __MenuLoop__ is a framework for a basic, repeating CLI menu-loop.

  

# py_util.collections

**collections** is probably my best-developed set of utilities.

* There are four __Base Classes__ (styled after _collections.UserDict_) that have a few ease-of-use modifications: _BaseCollection_, _BaseMapping_, _BaseSequence_, and _BaseSet_.

* **FilteredSet** is an abstract mixin-class that causes a set to fail to add some candidate elements, based on a specified condition.

* **JSONableMapping** is an abstract mixin-class that makes a dict-type object representable/ initialize-able from JSON.

* **TaggableCollection** is a mixin class that makes a collection able to tag its objects and provides a *parse( input_string)* method to read a tag structure.  Eventually, _TagStructure_ will be its own thing and _Taggable_ will be a lightweight wrapper over it, but _TaggableCollection_ works well enough for now.

* **ThreadDispatcher** is a subclass of _TaggableCollection_ where objects in the collection can be tagged for actions to be done to them.  As an example use-case, I've used this to make only certain parts of a data record updatable; the tagged-for actions were different data-update operations which could each be run on a different subset of the collection.

  

# py_util.decorators

**decorators** contains any functionality implemented as a decorator.  Currently only _common\_repr_ is implemented, but there are placeholder files for a few utilities that I plan to write: _function\_logger_, _function\_memoization_, and _function\_timer_.



# py_util.etc

**etc** contains utilities that do not fit well into any other category.

* **sql_utility.py** contains the *SQL\_Table* class, and is not a serious attempt to implement SQL functionality (this class was originally used to facilitate a school project),

* **thread_managers.py** contains a regular _ThreadManager_, _PatientThreadManager_ that starts each thread after a 0.1 second delay, and _BatchThreadManager_ that runs threads in fixed-size cohorts.

* I would prefer that each utility be located in a more-relevant context, so eventually _SQL_Table_ will be made a _py_util.collections_ mixin class and the thread managers will be moved to _py_util.concurrency_ (or whatever that folder is called when I create it).

  

# py_util.parsers

**parsers** contains any thing that extracts information from structured text.  

* **string_interpreters.py** has a few helper functions that do not warrant their own file. 
* **read_taggable_collection.py** is the parser that is used to build a class with the *TaggableCollection* mixin; *TaggableCollection.parse( input_string)* calls *py_util.parsers.read_taggable_collection( input_string)*.  The parser is here, separate from the rest of the class, because writing a formal grammar is a completely different type of problem than everything else that the *TaggableCollection* does. I am going to continue to keep parsers separate from the definition of the classes they build so that I can start to factor out different parsing functionalities into a toolkit.



# py_util.test

The **test** folder contains unit-tests, demonstration scripts, and a README that more-completely explains the test suite for anyone interested.
