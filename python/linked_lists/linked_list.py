from typing import Any
from pprint import pprint


class Node:
    """A node element containing a value and a reference to the next node."""

    def __init__(self, value) -> None:
        """Initialize node with given value."""
        self.value = value
        self.next = None

    def __repr__(self):
        """Node representation."""
        return "Node(value={}, next -> {})".format(self.value, repr(self.next))


class DoublyNode:
    """A node element containing a value and references to next and previous nodes."""

    def __init__(self, value) -> None:
        """Initialize node with given value and provide reference to previous and next."""
        self.value = value
        self.previous = None
        self.next = None

    def __repr__(self) -> str:
        """string representation."""
        return "DoublyLinkedList(id={}, value={}, previous={}, next={})".format(
            id(self),
            self.value,
            id(self.previous) if self.previous is not None else None,
            id(self.next) if self.next is not None else None,
        )


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

    def __str__(self) -> str:
        """Human readable string representation of linked list."""
        string = "["

        node = self.head
        while node is not None:
            string += str(node.value)
            if node.next is not None:
                string += " -> "
            node = node.next
        string += "]"

        return string

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

    def add_head(self, item: Any) -> None:
        """Add item on the head of the list."""
        try:
            node = Node(item)

            node.next = self.head
            self.head = node

        except Exception as exc:
            raise exc

    def add_tail(self, item: Any) -> None:
        """Add item on the tail of the list."""
        try:
            node = Node(item)

            tail = self.get_tail()

            if tail is None:
                self.head = node
            else:
                tail.next = node

        except Exception as exc:
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
        elif self.head.value == item:
            next_head = self.head.next
            del self.head
            self.head = next_head
        else:
            pointer = self.get_previous_pointer(item)
            next_replacement = pointer.next.next

            del pointer.next

            pointer.next = next_replacement

    def remove_all(self, item: Any) -> None:
        """Remove all occurrences of item on list."""

        if self.is_empty():
            raise ValueError("List is empty")

        elif self.is_singular():
            if self.head.value != item:
                raise ValueError("Item {} is not on list".format(item))
            else:
                self.head = None
        else:
            while item in self:
                try:
                    self.remove(item)
                except ValueError as exc:
                    break

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
            pointer = self.head

            while pointer is not None:
                items.append(pointer.value)
                pointer = pointer.next

            return items
        except Exception as exc:  # pragma no cover
            raise exc

    def get_count(self) -> int:
        """Get the count of total items on the linked list."""
        try:
            count = 0
            pointer = self.head

            while pointer is not None:
                count += 1
                pointer = pointer.next

            return count
        except Exception as exc:  # pragma no cover
            raise exc

    def empty(self) -> None:
        """Empty the list."""
        self.head = None


class DoublyLinkedList:
    """Doubly linked list."""

    def __init__(self, *items) -> None:
        """Initialize doubly linked list with values."""
        self.head = None
        for item in items:
            self.insert(item)

    def __str__(self) -> str:
        """Human readable string representation."""
        items = self.get_items()
        return str(items)

    def __repr__(self) -> str:
        pointer = self.head

        representation = "DoublyLinkedList("

        pointer = self.head

        while pointer is not None:
            representation += "Node(id={}, previous={}, value={}, next={})".format(
                id(pointer),
                id(pointer.previous) if pointer.previous is not None else None,
                pointer.value,
                id(pointer.next) if pointer.next is not None else None,
            )

            if pointer.next is not None:
                representation += " -> "

            pointer = pointer.next

        representation += ")"

        return representation

    def __contains__(self, item: Any) -> bool:
        """Check if item is on the list."""
        return item in self.get_items()

    def insert(self, item: Any) -> None:
        """Insert item on doubly linked list."""

        node = DoublyNode(item)

        if self.head is None:
            self.head = node
        else:
            tail = self.get_tail()
            tail.next = node
            node.previous = tail

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
        """Get value items on doubly linked list."""

        items = []
        pointer = self.head

        while pointer is not None:
            items.append(pointer.value)
            pointer = pointer.next

        return items

    def is_empty(self) -> bool:
        """Check if list is empty."""
        return self.head is None

    def get_count(self) -> int:
        count = 0
        pointer = self.head

        while pointer is not None:
            count += 1

        return count

    def empty(self):
        """Empty the list."""
        self.head = None

    def find(self, item: Any) -> DoublyNode:
        """Find the first node containing the item."""
        pointer = self.head

        while pointer is not None:
            if pointer.value == item:
                break
            pointer = pointer.next
        else:
            raise ValueError("item {} is not on list".format(item))

        return pointer

    def get_previous_pointer(self, item: Any) -> DoublyNode:
        """Find the node before the node containing the item."""
        node = self.find(item)

        pointer = node.previous

        return pointer

    def is_singular(self) -> bool:
        """Check if list is singular."""
        return not self.is_empty() and self.head.next is None

    def remove(self, item: Any) -> None:
        """Remove item on the list"""

        if self.is_empty():
            raise ValueError("List is empty")
        elif self.is_singular():
            if item == self.head.value:
                self.head = None
            else:
                raise ValueError("item {} is not on list".format(item))
        else:
            node = self.find(item)
            if node is self.head:
                self.head = node.next
                self.head.previous = None
            else:
                previous_pointer = self.get_previous_pointer(item)
                next_pointer = node.next

                previous_pointer.next = next_pointer
                if next_pointer is not None:
                    next_pointer.previous = previous_pointer

    def remove_all(self, item: Any):
        """Remove all nodes containing item on the linked list."""
        while item in self:
            self.remove(item)


singly = LinkedList(1, 2, 3)
doubly = DoublyLinkedList(1, 2, 3)
