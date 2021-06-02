from typing import Iterator
import unittest

from w3.python.core.fundamental_interface.DOMException import DOMException
from w3.python.core.fundamental_interface.Node import Node
from w3.python.core.fundamental_interface.Node import NodeType
from w3.python.core.fundamental_interface.NodeList import NodeList


def _make_nodes(n: int) -> Iterator[Node]:
    """Accessor to create `n` random nodes immediatly.

    Args:
        n: number of nodes to generate.

    Yields:
        A randomly generated node.
    """
    for _ in range(n):
        yield Node(NodeType.TEXT_NODE, '#text')


class Test_NodeList(unittest.TestCase):
    def testInit(self):
        NodeList()
        # Initiate with a node
        node = next(_make_nodes(1))
        NodeList([node])
        # Initiate with multiple nodes.
        NodeList(_make_nodes(4))

    def testIter(self):
        nodes = [*_make_nodes(4)]
        node_list = NodeList(nodes)
        # Create an iterator for checking
        node_iter = iter(nodes)
        for list_elem in node_list:
            self.assertEqual(list_elem, next(node_iter))

    def testItem_inSize(self):
        nodes = [*_make_nodes(5)]
        node_list = NodeList(nodes)
        for i in range(5):
            self.assertEqual(node_list.item(i), nodes[i])

    def testItem_greaterOrEqualThanSize(self):
        node_list = NodeList(_make_nodes(5))
        for i in range(5, 8):
            self.assertIsNone(node_list.item(i))

    def testItem_notValid(self):
        node_list = NodeList(_make_nodes(5))
        for idx in [-1, -9999, 'hi', '1', None, Node, NodeList, b'0']:
            self.assertIsNone(node_list.item(idx))

    def testLength(self):
        # Empty NodeList
        node_list = NodeList()
        self.assertEqual(node_list.length, 0)
        # NodeList with a node.
        node_list = NodeList(_make_nodes(1))
        self.assertEqual(node_list.length, 1)
        # NodeList with some items.
        node_list = NodeList(_make_nodes(5))
        self.assertEqual(node_list.length, 5)


if __name__ == '__main__':
    unittest.main()
