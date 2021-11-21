class Node:
    """A node element containing a value and a reference to the next node."""

    def __init__(self, value) -> None:
        """Initialize node with given value."""
        self.value = value
        self.next = None

    def __repr__(self):
        """Node representation."""
        return "Node(value={}, next -> {})".format(self.value, repr(self.next))
