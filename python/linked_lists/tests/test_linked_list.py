from python.linked_lists.node import Node
from python.linked_lists.linked_list import LinkedList


def test_repr():
    """Test repr method."""
    linked_list = LinkedList()

    expected = "LinkedList({})".format(repr(linked_list.head))

    assert expected == repr(linked_list)


def test_insert_empty_list():
    """Insert item should be added to list."""
    linked_list = LinkedList()

    item = 1

    linked_list.insert(1)

    assert isinstance(linked_list.head, Node)
    assert linked_list.head.value == item


def test_is_empty_returns_True_on_empty_list():
    """is_empty() method returns True on empty list."""

    linked_list = LinkedList()

    assert linked_list.is_empty()


def test_is_empty_returns_False_on_non_empty_list():
    """is_empty() method returns False on non empty list."""

    linked_list = LinkedList()
    linked_list.insert(1)

    assert not linked_list.is_empty()
