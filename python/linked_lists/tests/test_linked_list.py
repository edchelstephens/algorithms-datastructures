import pytest
from pprint import pprint

from python.linked_lists.node import Node
from python.linked_lists.linked_list import LinkedList


def test_repr() -> None:
    """Test repr method."""
    linked_list = LinkedList()

    expected = "LinkedList({})".format(repr(linked_list.head))

    assert expected == repr(linked_list)


def test_linked_list_creates_linked_nodes_of_items() -> None:
    """LinkedList creates a linked list of nodes of items."""

    items = [1, 2, 3]

    linked_list = LinkedList(*items)

    list_items = []

    head = linked_list.head

    while head is not None:
        list_items.append(head.value)
        head = head.next

    assert items == list_items


def test_insert_empty_list() -> None:
    """Insert item should be added to list."""
    linked_list = LinkedList()

    item = 1

    linked_list.insert(1)

    assert isinstance(linked_list.head, Node)
    assert linked_list.head.value == item


def test_insert_inserts_item_as_head_on_empty_linked_list() -> None:
    """insert() inserts item as head on empty linked list."""

    item = 1

    linked_list = LinkedList()
    linked_list.insert(item)

    assert not linked_list.is_empty()
    assert isinstance(linked_list.head, Node)
    assert linked_list.head.value == item


def test_insert_successfully_adds_item_on_tail_of_non_empty_linked_list() -> None:
    """insert() adds item on the tail of the linked list."""

    item = 2

    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)

    assert linked_list.get_tail().value == item


def test_is_empty_returns_True_on_empty_list() -> None:
    """is_empty() method returns True on empty list."""

    linked_list = LinkedList()

    assert linked_list.is_empty()


def test_is_empty_returns_False_on_non_empty_list() -> None:
    """is_empty() method returns False on non empty list."""

    linked_list = LinkedList()
    linked_list.insert(1)

    assert not linked_list.is_empty()


def test_get_tail_returns_None_on_empty_list() -> None:
    """get_tail() returns None on empty list."""

    linked_list = LinkedList()

    assert linked_list.get_tail() is None


def test_get_items_returns_a_list() -> None:
    """get_items() returns a list."""

    linked_list = LinkedList()

    assert isinstance(linked_list.get_items(), list)


def test_get_items_returns_empty_list_on_empty_linked_list() -> None:
    """get_items() returns an empty list on empty linked_list"""

    linked_list = LinkedList()

    assert linked_list.get_items() == []


def test_get_items_retrieves_the_node_items_on_the_list() -> None:
    """get_items() returns the list of node items on the linked list."""

    items = [1, 2, 3]

    linked_list = LinkedList(*items)

    assert linked_list.get_items() == items


def test_get_count_returns_0_on_empty_list() -> None:
    """get_count() returns 0 on empty list."""

    linked_list = LinkedList()

    assert linked_list.get_count() == 0


def test_get_count_returns_actual_count_of_initiliazed_items_on_linked_list() -> None:
    """get_count() returns returns the actual length of initialized items on the list."""

    items = [1, 2, 3]
    linked_list = LinkedList(*items)

    assert linked_list.get_count() == len(items)


def test_get_count_returns_actual_count_of_items_on_linked_list() -> None:
    """get_count() returns gets the actual count of items in the list."""

    items = [1, 2, 3]
    initial_count = len(items)

    linked_list = LinkedList(*items)

    linked_list.insert(4)
    linked_list.insert(5)

    insertions = 2

    assert linked_list.get_count() == initial_count + insertions


def test_in_list_returns_False_on_item_not_on_list() -> None:
    """item not in list should return false on in check."""

    items = [1, 2, 3]

    linked_list = LinkedList(*items)

    assert 4 not in linked_list


def test_in_list_returns_True_on_item_in_list() -> None:
    """item not in list should return false on in check."""

    items = [1, 2, 3]

    linked_list = LinkedList(*items)

    for item in items:
        assert item in linked_list


def test_remove_raises_exception_on_trying_to_remove_an_item_on_empty_list() -> None:
    """remove() raises ValueError when trying to remove something on an empty list"""

    linked_list = LinkedList()

    with pytest.raises(ValueError):
        linked_list.remove(1)


def test_remove_raises_exception_on_trying_to_remove_non_existent_item_on_list() -> None:
    """remove() raises ValueError when trying to remove an item that is non existent in the list."""

    items = [1, 2]
    linked_list = LinkedList(*items)

    with pytest.raises(ValueError):
        linked_list.remove(3)


def test_remove_removes_singular_item_on_list() -> None:
    """remove() removes single item on list."""

    linked_list = LinkedList(1)

    linked_list.remove(1)

    assert 1 not in linked_list
    assert linked_list.get_items() == []


def test_remove_removes_item_on_a_multi_list() -> None:
    """remove() removes item on the list."""

    linked_list = LinkedList(1, 2, 3, 4)

    linked_list.remove(4)

    assert 4 not in linked_list
    assert linked_list.get_items() == [1, 2, 3]


def test_find_raises_value_error_on_finding_something_on_an_empty_list() -> None:
    """find() raises ValueError on trying to find something on an empty list."""

    linked_list = LinkedList()

    with pytest.raises(ValueError):
        linked_list.find(1)


def test_find_raises_value_error_on_trying_to_find_node_item_which_does_not_exist_on_list() -> None:
    """find() raises ValueError if item node does not exist."""

    items = [1, 2]

    linked_list = LinkedList(*items)
    with pytest.raises(ValueError):
        linked_list.find(3)


def test_find_returns_a_Node_on_a_found_item_on_the_list() -> None:
    """find() returns a Node object if item found on list."""

    items = [1, 2, 3]

    linked_list = LinkedList(*items)

    node = linked_list.find(1)

    assert isinstance(node, Node)


def test_find_returns_the_Node_containing_the_node_item_on_the_list() -> None:
    """find() returns a Node object containing the item on the list."""

    items = [1, 2, 3]

    linked_list = LinkedList(*items)

    node = linked_list.find(1)

    assert node.value == 1


def test_get_previous_pointer_empty_list() -> None:
    """get_previous_pointer() raises ValueError on empty list."""
    linked_list = LinkedList()

    with pytest.raises(ValueError):
        linked_list.get_previous_pointer(1)


def test_get_previous_pointer_item_not_on_list() -> None:
    """get_previous_pointer() raises ValueError on trying to find previous pointer of item not on list."""
    items = [1, 2]
    linked_list = LinkedList(*items)

    with pytest.raises(ValueError):
        linked_list.get_previous_pointer(3)


def test_get_previous_pointer_item_on_list() -> None:
    """get_previous_pointer() returns the node pointing the next node containing the item."""

    items = [1, 2]
    linked_list = LinkedList(*items)

    pointer = linked_list.get_previous_pointer(2)

    assert isinstance(pointer, Node)
    assert pointer.next.value == 2


def test_get_previous_pointer_singular_item_on_list() -> None:
    """get_previous_pointer() returns the node pointing the single node containing the item."""

    items = [1]
    linked_list = LinkedList(*items)

    pointer = linked_list.get_previous_pointer(1)

    assert isinstance(pointer, Node)
    assert pointer.next is None
    assert pointer.value == 1


def test_get_previous_pointer_singular_item_not_on_list() -> None:
    """get_previous_pointer() raises ValueError on single item list which is not the lookup item."""

    items = [1]
    linked_list = LinkedList(*items)

    with pytest.raises(ValueError):
        linked_list.get_previous_pointer(2)


def test_is_singular_empty_list() -> None:
    """is_singular() returns False on empty list."""

    linked_list = LinkedList()

    assert not linked_list.is_singular()


def test_is_singular_singular_item_on_list() -> None:
    """is_singular() returns True on singular list."""

    linked_list = LinkedList(1)

    assert linked_list.is_singular()


def test_is_singular_multiple_item_list() -> None:
    """is_singular() returns False on multiple item list."""

    linked_list = LinkedList(1, 2, 3)

    assert not linked_list.is_singular()
