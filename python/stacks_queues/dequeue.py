from typing import Any


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


class DoublyLinkedList:
    """Doubly linked list."""

    def __init__(self, *items) -> None:
        """Initialize doubly linked list with values."""
        self.head = None
        self._count = 0
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
        return self.find(item) is not None

    def insert(self, item: Any) -> None:
        """Insert item on doubly linked list."""

        node = DoublyNode(item)

        if self.head is None:
            self.head = node
        else:
            tail = self.get_tail()
            tail.next = node
            node.previous = tail

        self._count += 1

    def add_head(self, item: Any) -> None:
        """Insert item on the head of the list."""
        try:
            node = DoublyNode(item)

            node.next = self.head
            self.head = node

            self._count += 1

        except Exception as exc:
            raise exc

    def add_tail(self, item: Any) -> None:
        """Insert item on the tail of the list."""

        node = DoublyNode(item)

        tail = self.get_tail()

        if tail is None:
            self.head = node
        else:
            node.previous = tail
            tail.next = node

        self._count += 1

    def remove_head(self) -> None:
        """Remove the item on the head."""

        if self.is_empty():
            pass
        elif self.is_singular():
            del self.head
            self.head = None
            self._count -= 1
        else:
            head = self.head
            next_head = head.next
            next_head.previous = None
            self.head = next_head

            self._count -= 1

    def remove_tail(self) -> None:
        """Remove the item on the tail."""

        if self.is_empty():
            pass
        elif self.is_singular():
            del self.head
            self.head = None
            self._count -= 1
        else:
            tail = self.get_tail()
            previous = tail.previous
            del tail
            previous.next = None
            self._count -= 1

    def get_tail(self) -> DoublyNode | None:
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
        return self._count

    def empty(self):
        """Empty the list."""
        self.head = None

    def find(self, item: Any) -> DoublyNode:
        """Find the first node containing the item."""
        try:
            found_node = None
            node = self.head

            while node is not None:
                if node.value == item:
                    found_node = node
                    break
                node = node.next

            return found_node
        except Exception as exc:
            return None

    def get_previous_pointer(self, item: Any) -> DoublyNode:
        """Find the node before the node containing the item."""

        found_node = None

        node = self.find(item)

        if node is not None:
            found_node = node.previous

        return found_node

    def is_singular(self) -> bool:
        """Check if list is singular."""
        return not self.is_empty() and self.head.next is None

    def remove(self, item: Any) -> bool:
        """Remove item on the list"""
        is_removed = False

        if self.is_empty():
            is_removed = False
        elif self.is_singular():
            if item == self.head.value:
                self.head = None
                is_removed = True
        else:
            node = self.find(item)
            if node is self.head:
                self.head = node.next
                self.head.previous = None
                is_removed = True
            else:
                previous_pointer = self.get_previous_pointer(item)

                if previous_pointer is not None:
                    next_pointer = node.next

                    previous_pointer.next = next_pointer
                    if next_pointer is not None:
                        next_pointer.previous = previous_pointer

                    is_removed = True

        self._count -= 1

        return is_removed

    def remove_all(self, item: Any) -> int:
        """Remove all nodes containing item on the linked list.

        Returns the count of items removed.
        """
        count = 0
        while item in self:
            self.remove(item)
            count += 1
        return count


class Dequeue:
    """A double ended queue, which can perform both first-in, first-out, or last-in, last-out."""

    def __init__(self, *items) -> None:
        self.store = DoublyLinkedList(*items)

    def __repr__(self) -> str:
        return "Dequeue: {}".format(self.get_items())

    def get_items(self) -> list:
        """Get the items of the queue."""
        return self.store.get_items()

    def enqueue_head(self, item: Any) -> None:
        """Add item on the head."""
        self.store.add_head(item)

    def enqueue_tail(self, item: Any) -> None:
        """Add item on the tail."""
        self.store.add_tail(item)

    def dequeue_head(self) -> None:
        """Remove item on the head."""
        self.store.remove_head()

    def dequeue_tail(self) -> None:
        """Remove item on the tail"""
        self.store.remove_tail()

    def get_count(self) -> int:
        """Get the count of items on the queue"""
        return self.store.get_count()

    def peek_head(self) -> Any:
        """Get the head item without dequeuing it."""

        head = self.store.head
        value = None
        if head is not None:
            value = head.value

        return value

    def peek_tail(self) -> Any:
        """Get the tail item without dequeuing it."""

        tail = self.store.get_tail()

        value = None

        if tail is not None:
            value = tail.value

        return value
