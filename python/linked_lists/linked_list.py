from typing import Any

from python.linked_lists.node import Node


class LinkedList:
    """Linked list class."""

    def __init__(self, *items, **kwargs):
        """Construct linked list from given items."""
        self.head = None

    def __repr__(self) -> str:
        """String representation of linked list."""
        return "LinkedList({})".format(self.head)

    def insert(self, item: Any) -> None:
        """Insert item to linked list."""
        if self.is_empty():
            self.head = Node(item)

    def is_empty(self) -> bool:
        """Check if list is empty."""
        return self.head is None
