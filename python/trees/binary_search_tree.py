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
        """Apply action on the tree nodes in pre-order."""
        if node is not None:
            action(node.value)
            self.pre_order(action, node.left)
            self.pre_order(action, node.right)

    def print_pre_order(self) -> None:
        """Print the binary search tree in pre-order traversal."""
        self.pre_order(print, self.root)

    def in_order(self, action: Callable, node: BinaryTreeNode) -> None:
        """Apply action on the tree nodes in in-order."""
        if node is not None:
            self.in_order(action, node.left)
            action(node.value)
            self.in_order(action, node.right)

    def print_in_order(self) -> None:
        """Traverse and print the tree in-order."""
        self.in_order(print, self.root)

    def post_order(self, action: Callable, node: BinaryTreeNode) -> None:
        """Apply action on the tree nodes in post order"""

        if node is not None:
            self.post_order(action, node.left)
            self.post_order(action, node.right)
            action(node.value)

    def print_post_order(self) -> None:
        """Traverse and print the tree in post-order."""
        self.post_order(print, self.root)

    def get_count(self) -> None:
        """Get the count of nodes in the tree."""
        return self._count


# A binary search tree
#    12
#  7   14
# 3 7    18
b = BinarySearchTree()
b.root = BinaryTreeNode(12)
b.root.left = BinaryTreeNode(7)
b.root.left.left = BinaryTreeNode(3)
b.root.left.right = BinaryTreeNode(7)
b.root.right = BinaryTreeNode(14)
b.root.right.right = BinaryTreeNode(18)


print("=== Pre order ===")
b.print_pre_order()
print()
# b.print_pre_order()
# 12 7 3 7 14 18

# 12
# 7
# 3
# 7
# 14
# 18

print("=== In order ===")
b.print_in_order()
print()
# b.print_in_order()
# 3 7 7 12 14 18

# 3
# 7
# 7
# 12
# 14
# 18

print("=== Post order ===")
b.print_post_order()
print()
# b.print_post_order()
# 3 7 7 18 14 12

# 3
# 7
# 7
# 18
# 14
# 12
