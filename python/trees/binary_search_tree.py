from typing import Any, Callable


class BinaryTreeNode:
    """A binary tree node."""

    def __init__(self, value: Any, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return "BinaryTreeNode(value={}, left={}, right={})".format(
            self.value,
            id(self.left) if self.left is not None else None,
            id(self.right) if self.right is not None else None,
        )


class BinarySearchTree:
    """A binary search tree data structure."""

    def __init__(self, *items) -> None:
        self.root = None
        self._count = 0
        for item in items:
            self.insert(item)
            self._count += 1

    def insert(self, item: Any) -> None:
        """Insert item on the binary search tree."""

        node = BinaryTreeNode(item)

        if self.root is None:
            self.root = node
        else:
            pointer = self.root

            raise NotImplementedError

        self._count += 1

    def pre_order(self, action: Callable, node: BinaryTreeNode) -> None:
        """Traverse the node in pre-order, and do action."""
        if node is not None:
            action(node.value)
            self.pre_order(action, node.left)
            self.pre_order(action, node.right)

    def print_pre_order(self) -> None:
        """Print the binary search tree in pre-order traversal."""
        self.pre_order(print, self.root)

    def get_count(self) -> None:
        """Get the count of nodes in the tree."""
        return self._count
