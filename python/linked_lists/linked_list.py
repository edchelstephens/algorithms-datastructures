from typing import Any

from python.linked_lists.node import Node


class LinkedList:
    """Linked list class."""

    def __init__(self, *items, **kwargs):
        """Construct linked list from given items."""
        try:
            self.head = None
            for item in items:
                self.insert(item)
        except Exception as exc:  # pragma no cover
            raise exc

    def __repr__(self) -> str:
        """String representation of linked list."""
        return "LinkedList({})".format(self.head)

    def insert(self, item: Any) -> None:
        """Insert item to linked list."""
        try:
            node = Node(item)

            if self.is_empty():
                self.head = node
            else:
                tail = self.get_tail()
                tail.next = node

        except Exception as exc:  # pragma no cover
            raise exc

    def is_empty(self) -> bool:
        """Check if list is empty."""
        try:
            return self.head is None
        except Exception as exc:  # pragma no cover
            raise exc

    def get_tail(self) -> Node | None:
        """Return the last node in the linked list."""
        try:

            tail = self.head

            if tail is not None:
                while tail.next is not None:
                    tail = tail.next

            return tail
        except Exception as exc:  # pragma no cover
            raise exc
