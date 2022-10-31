import uuid

class Element:
    """This represents any physical element that can appear in an Environment.
    You subclass Element to get the things you want. Each elem can have a
    .__name__  slot (used for output only)."""

    def __init__(self):
        self.id = uuid.uuid1() # Random unique identifier to an element

    def __repr__(self):
        return '<{}>'.format(getattr(self, '__name__', self.__class__.__name__))

    def is_alive(self):
        """Things that are 'alive' should return true."""
        return hasattr(self, 'alive') and self.alive

    def show_state(self):
        """Display the agent's internal state. Subclasses should override."""
        print("I don't know how to show_state.")