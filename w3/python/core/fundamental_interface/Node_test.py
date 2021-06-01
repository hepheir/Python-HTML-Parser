import unittest

from w3.python.core.fundamental_interface.Node import Node
from w3.python.core.fundamental_interface.Node import NodeType


class Test_Node(unittest.TestCase):
    def test_init(self):
        node = Node(node_type=NodeType.DOCUMENT_NODE,
                    node_name='#document',
                    read_only=False)
        self.assertEqual(node.node_type, NodeType.DOCUMENT_NODE)
        self.assertEqual(node.node_name, '#document')
        self.assertEqual(node.node_value, '')

    def testNodeType_get(self):
        for node_type in NodeType:
            node = Node(node_type=node_type,
                        node_name='')
            self.assertEqual(node.node_type, node_type)

    def testNodeType_setCorrectTypes(self):
        for node_type in NodeType:
            node = Node(node_type=node_type,
                        node_name='')
            self.assertEqual(node.node_type, node_type)

    def testNodeType_setWrongTypes(self):
        for node_type in [-1, None, 'hi', Node, True, NodeType, 'DOCUMENT_NODE']:
            with self.assertRaises(TypeError):
                Node(node_type=node_type,
                     node_name='')


if __name__ == '__main__':
    unittest.main()
