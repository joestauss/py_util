from py_util.classes import TaggableCollection
import collections
import collections.abc

class ThreadDispatcher( TaggableCollection):
    """This mixin class enables thead-based actions, such as updating records.  Actions can be flagged to be batched.

    To make an ActionThreads perform an action:
    1)  Choose a tag for that action (EXAMPLE_ACTION_TAG below).
    2)  Write a method to perform the action ( example_method( seld) below).
    3)  Add the following key-value pair:
            ACTION_TAG : CORRESPONDING_METHOD_NAME
        to either the regular_action_tags or batch_action_tags dictionary.



    Workflow
    ========
        1.  Tag objects in the collection for actions.
        2.  Call "do_all_actions" or whatever.
        3.  for each tag, data in action_tags:
        4.      for record in data:
        5.          self.batch_actions[ tag]( record)

    Each batch action should be a static method.
    """ #v1

    @property
    def action_tags( self):
        return {t for t in self.tags if t in self.regular_actions or self.batch_actions}

    @property
    def action_threads( self):
        regular_threads  = []
        batch_threads    = []
        for tag, perform_action in self.regular_actions:
            if tag in self.tags:
                tagged_items = self.tags[ tag]
                batch_threads.extend( [ threading.Thread( target=perform_action(item)) for item in tagged_items])
        for tag, perform_action in self.batch_actions:
            if tag in self.tags:
                tagged_items = self.tags[ tag]
                batch_threads.extend( [ threading.Thread( target=perform_action(item)) for item in tagged_items])
        return regular_threads, batch_threads

    def dispatch_all( self, VERBOSE=False):
        """Do all actions on all records in this object."""
        regular_threads, batch_threads = self.action_threads
        PatientThreadManager(regular_threads)(VERBOSE=VERBOSE)
        BatchThreadManager(batch_threads)(VERBOSE=VERBOSE)

    #   Subclasses must implement the following:
    #
    def example_method( self):
        pass

    EXAMPLE_ACTION_TAG =  "ACTION TAG - Example." # a hash to avoid accidental collision

    regular_actions = {
        EXAMPLE_ACTION_TAG : example_method
    }
    batch_actions = {}
    #
    #   End of subclass requirements.
