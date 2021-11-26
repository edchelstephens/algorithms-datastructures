from pprint import pprint

from python.linked_lists.node import Node
from python.linked_lists.linked_list import LinkedList


def test_repr():
    """Test repr method."""
    linked_list = LinkedList()

    expected = "LinkedList({})".format(repr(linked_list.head))

    assert expected == repr(linked_list)


def test_linked_list_creates_linked_nodes_of_items():
    """LinkedList creates a linked list of nodes of items."""

    items = [1, 2, 3]

    linked_list = LinkedList(*items)

    list_items = []

    head = linked_list.head

    while head is not None:
        list_items.append(head.value)
        head = head.next

    assert items == list_items


def test_insert_empty_list():
    """Insert item should be added to list."""
    linked_list = LinkedList()

    item = 1

    linked_list.insert(1)

    assert isinstance(linked_list.head, Node)
    assert linked_list.head.value == item


def test_insert_inserts_item_as_head_on_empty_linked_list():
    """insert() inserts item as head on empty linked list."""

    item = 1

    linked_list = LinkedList()
    linked_list.insert(item)

    assert not linked_list.is_empty()
    assert isinstance(linked_list.head, Node)
    assert linked_list.head.value == item


def test_insert_successfully_adds_item_on_tail_of_non_empty_linked_list():
    """insert() adds item on the tail of the linked list."""

    item = 2

    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)

    assert linked_list.get_tail().value == item


def test_is_empty_returns_True_on_empty_list():
    """is_empty() method returns True on empty list."""

    linked_list = LinkedList()

    assert linked_list.is_empty()


def test_is_empty_returns_False_on_non_empty_list():
    """is_empty() method returns False on non empty list."""

    linked_list = LinkedList()
    linked_list.insert(1)

    assert not linked_list.is_empty()


def test_get_tail_returns_None_on_empty_list():
    """get_tail() returns None on empty list."""

    linked_list = LinkedList()

    assert linked_list.get_tail() is None
