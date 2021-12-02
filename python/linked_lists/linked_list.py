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
        if self.is_empty():
            raise ValueError("Linked list is empty.")
        elif self.is_singular():
            if self.head.value != item:
                raise ValueError("Item {} not on list".format(item))
            else:
                self.head = None
        else:
            pointer = self.get_previous_pointer(item)
            next_replacement = pointer.next.next

            del pointer.next

            pointer.next = next_replacement

    def find(self, item: Any) -> Node:
        """Find and return the first node containing the item on the list.

        Raises ValueError if item is not found on the list.
        """
        if self.is_empty():
            raise ValueError("Linked list is empty.")
        else:
            node = self.head

            while node is not None:
                if node.value == item:
                    break
                node = node.next
            else:
                raise ValueError("Item {} is not on list".format(item))

            return node

    def get_previous_pointer(self, item: Any) -> Node:
        """Get previous pointer of the first node containing item on the list.

        Raises ValueError if item is not found on the list.
        """
        if self.is_empty():
            raise ValueError("Linked list is empty.")
        elif self.is_singular():
            if self.head.value != item:
                raise ValueError("Item {} is not on list".format(item))
            return self.head
        else:

            node = self.head

            while node.next is not None:
                if node.next.value == item:
                    break
                node = node.next
            else:
                raise ValueError("Item {} is not on list".format(item))

            return node

    def is_empty(self) -> bool:
        """Check if list is empty."""
        try:
            return self.head is None
        except Exception as exc:  # pragma no cover
            raise exc

    def is_singular(self) -> bool:
        """Check if list contains single item."""
        return not self.is_empty() and self.head.next is None

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
