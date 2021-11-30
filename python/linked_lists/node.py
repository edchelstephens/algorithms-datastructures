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
        """Doubly node representation."""
        return """Node(prev -> {}, value={}, next -> {}""".format(
            self.previous, self.value, self.next
        )
