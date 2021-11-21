from python.linked_lists.node import Node


def test_node_repr():

    node = Node(1)

    expected = "Node(value={}, next={})".format(node.value, repr(node.next))

    assert expected == repr(node)
