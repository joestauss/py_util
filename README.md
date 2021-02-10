# my-python-utilities

This repository contains various general-purpose python tools that I use.


# Folders

# py_util.classes

This folder contains three base classes (_BaseRecord_, _BaseCollection_, and _BaseSequence_), as well as the mix-in classes _FilteredSet_ and _JSONableMapping_.

# py_util.cli

* __boxed\_text__ is a pretty-print function that puts its args in a box.  Any iterables are unpacked and everything is given its own line.

* __cli\_selector__ gets a user's input from among a list of options.  It supports two modes of operation:
 - _single_ - User selects a single choice.  This is the default mode.
 - _many_ - User can input several choices separated by a comma.

*  __MenuLoop__ is a framework for a basic, repeating CLI menu-loop.

# py_util.decorators

**decorators** contains any function implemented as a decorator.  Currently, only _common\_repr_ is implemented, but there are placeholder files for _function\_logger_, _function\_memoization_, and _function\_timer_

## py_util.etc
**etc** contains utilities that do not fit well into any other category.

* **sql_utility.py** contains the *SQL\_Table* class.  This class was originally used to facilitate a school project, and is not a serious attempt to implement SQL.
* **thread_managers.py** contains a regular _ThreadManager_, _PatientThreadManager_ that starts each thread after a 0.1 second delay, and _BatchThreadManager_ that runs threads fixed-size cohorts.
* This folder also contains files for the unimplemented utilities *dir\_mgr*, *image\_browser*, and *image\_downloader*.

## py_util.test

The **test** folder contains both unit-tests and scripts to demonstrate program behavior.  Unit-tests are titled ("ut.\_.py") and demonstrations are titled ("demo.\_.py").  The structure of the *test* folder mirrors the structure of the rest of the package so, for example, all of the files in *py\_util/cli* are tested in *py\_util/test/cli*.
