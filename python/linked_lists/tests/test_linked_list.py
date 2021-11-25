from python import linked_lists
from python.linked_lists.linked_list import LinkedList


def test_repr():
    """Test repr method."""
    linked_list = LinkedList()

    expected = "LinkedList({})".format(repr(linked_list.head))

    assert expected == repr(linked_list)
