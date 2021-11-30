from typing import Any

from python.linked_lists.node import Node


class LinkedList:
    """Singly linked list."""

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

    def __contains__(self, item: Any) -> bool:
        """Check if item is on the list."""
        return item in self.get_items()

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

    def remove(self, item: Any) -> None:
        """Remove node containing item on the list."""
        if self.is_empty() or item not in self.get_items():
            raise ValueError("item {} not in list".format(item))
        else:
            pass

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

    def get_items(self) -> list:
        """Return a list of items for the node values on the linked list."""
        try:
            items = []
            head = self.head

            while head is not None:
                items.append(head.value)
                head = head.next

            return items
        except Exception as exc:  # pragma no cover
            raise exc

    def get_count(self) -> int:
        """Get the count of total items on the linked list."""
        try:
            count = 0
            head = self.head

            while head is not None:
                count += 1
                head = head.next

            return count
        except Exception as exc:  # pragma no cover
            raise exc


class DoublyLinkedList:
    """Doubly linked list."""

    def __init__(self, *items) -> None:
        """Initialize doubly linked list with values."""
        for item in items:
            self.insert(item)

    def insert(self, item: Any) -> None:
        """Insert item on doubly linked list."""
        pass
