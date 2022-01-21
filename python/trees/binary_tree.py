from turtle import right
from typing import Any


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
