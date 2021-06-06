from typing import Iterator, Optional
import unittest

from w3.dom import Node
from w3.dom import NodeType
from w3.dom import NodeList


def _create_document_node():
    return Node(node_type=NodeType.DOCUMENT_NODE,
                node_name='#document',
                owner_document=None)


def _create_text_node(document: Node):
    assert document.node_type == NodeType.DOCUMENT_NODE
    return Node(node_type=NodeType.TEXT_NODE,
                node_name='#text',
                owner_document=document)


def _make_nodes(n: int, document: Optional[Node] = None) -> Iterator[Node]:
    """Accessor to create `n` random nodes immediatly.

    Args:
        n: number of nodes to generate.

    Yields:
        A randomly generated node.
    """
    if document is None:
        document = _create_document_node()
    for _ in range(n):
        yield _create_text_node(document)


class Test_Dunder(unittest.TestCase):
    def testInit_Empty(self):
        NodeList()

    def testInit_SingleNode(self):
        node = next(_make_nodes(1))
        NodeList([node])

    def testInit_MultipleNodes(self):
        NodeList(_make_nodes(4))

    def testIter(self):
        nodes = [*_make_nodes(4)]
        node_list = NodeList(nodes)
        # Create an iterator for checking
        node_iter = iter(nodes)
        for list_elem in node_list:
            self.assertEqual(list_elem, next(node_iter))

    def testBool(self):
        # Empty `NodeList` should equal False.
        node_list = NodeList()
        self.assertFalse(node_list)
        # `NodeList` with items should equal True.
        node_list = NodeList(_make_nodes(2))
        self.assertTrue(node_list)

    def testGetItem(self):
        nodes = [*_make_nodes(4)]
        node_list = NodeList(nodes)
        for i in range(4):
            self.assertEqual(node_list[i], nodes[i])

    def testSetItem(self):
        document = _create_document_node()
        text_node = _create_text_node(document)
        node_list = NodeList(_make_nodes(4, document))
        node_list[2] = text_node
        self.assertEqual(node_list[2], text_node)

    def testContains(self):
        nodes = [*_make_nodes(4)]
        node_list = NodeList(nodes)
        for n in node_list:
            self.assertIn(n, node_list)

    def testContains_NotIn(self):
        internal_nodes = [*_make_nodes(4)]
        external_node = _make_nodes(1)
        node_list = NodeList(internal_nodes)
        self.assertNotIn(external_node, node_list)


class Test_Length(unittest.TestCase):
    def test_Empty(self):
        node_list = NodeList()
        self.assertEqual(node_list.length, 0)

    def test_OneItem(self):
        node_list = NodeList(_make_nodes(1))
        self.assertEqual(node_list.length, 1)

    def test_SomeItems(self):
        node_list = NodeList(_make_nodes(5))
        self.assertEqual(node_list.length, 5)


class Test_Item(unittest.TestCase):
    def test_InSize(self):
        nodes = [*_make_nodes(5)]
        node_list = NodeList(nodes)
        for i in range(5):
            self.assertEqual(node_list.item(i), nodes[i])

    def test_GreaterOrEqualThanSize(self):
        node_list = NodeList(_make_nodes(5))
        for i in range(5, 8):
            self.assertIsNone(node_list.item(i))

    def test_InvalidIndex(self):
        node_list = NodeList(_make_nodes(5))
        for idx in [-1, -9999, 'hi', '1', None, Node, NodeList, b'0']:
            self.assertIsNone(node_list.item(idx))


if __name__ == '__main__':
    unittest.main()
