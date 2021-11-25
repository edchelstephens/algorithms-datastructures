from python.linked_lists.node import Node


class LinkedList:
    """Linked list class."""

    def __init__(self, *items, **kwargs):
        """Construct linked list from given items."""
        self.head = None

    def __repr__(self) -> str:
        """String representation of linked list."""
        return "LinkedList({})".format(self.head)

    def insert(self, item) -> None:
        """Insert item to linked list."""
        if self.head is None:
            self.head = Node(item)
