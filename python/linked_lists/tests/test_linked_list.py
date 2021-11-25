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
