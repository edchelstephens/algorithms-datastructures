class LinkedList:
    """Linked list class."""

    def __init__(self, *items, **kwargs):
        """Construct linked list from given items."""
        self.head = None

    def __repr__(self) -> str:
        """String representation of linked list."""
        return "LinkedList({})".format(self.head)
