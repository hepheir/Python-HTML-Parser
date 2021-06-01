import unittest

from w3.python.core.fundamental_interface.DOMException import DOMException
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

    def testNodeValue_get(self):
        node = Node(node_type=NodeType.TEXT_NODE,
                    node_name='#text',
                    node_value='lorem ipsum')
        self.assertEqual(node.node_value, 'lorem ipsum')

    def testNodeValue_set(self):
        # set value from constructor
        node = Node(node_type=NodeType.TEXT_NODE,
                    node_name='#text',
                    node_value='foo',
                    read_only=False)
        self.assertEqual(node.node_value, 'foo')
        # set using setter
        node.node_value = 'bar'
        self.assertEqual(node.node_value, 'bar')

    def testNodeValue_setReadOnly(self):
        node = Node(node_type=NodeType.TEXT_NODE,
                    node_name='#text',
                    node_value='foo',
                    read_only=True)
        try:
            node.node_value = 'bar'
        except DOMException as e:
            code = e.args[0]
            self.assertEqual(code, DOMException.NO_MODIFICATION_ALLOWED_ERR)
        else:
            self.fail()
        # `node_value` should not be modified.
        self.assertEqual(node.node_value, 'foo')

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
