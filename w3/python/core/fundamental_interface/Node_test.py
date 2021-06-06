import unittest

from w3.dom import DOMException
from w3.dom import Node
from w3.dom import NodeType


def _create_document_node():
    return Node(node_type=NodeType.DOCUMENT_NODE,
                node_name='#document',
                owner_document=None)


def _create_element_node(document: Node):
    assert document.node_type == NodeType.DOCUMENT_NODE
    return Node(node_type=NodeType.ELEMENT_NODE,
                node_name='tagName',
                owner_document=document)


class Test_Dunder(unittest.TestCase):
    def testInit(self):
        # Creating document node.
        document = Node(node_type=NodeType.DOCUMENT_NODE,
                        node_name='#document',
                        owner_document=None,
                        read_only=False)
        self.assertEqual(document.node_type, NodeType.DOCUMENT_NODE)
        self.assertEqual(document.node_name, '#document')
        self.assertEqual(document.node_value, '')


class Test_NodeValue(unittest.TestCase):
    def testGetter(self):
        document = _create_document_node()
        text = Node(node_type=NodeType.TEXT_NODE,
                    node_name='#text',
                    owner_document=document,
                    node_value='lorem ipsum')
        self.assertEqual(text.node_value, 'lorem ipsum')

    def testConstructor(self):
        document = _create_document_node()
        text = Node(node_type=NodeType.TEXT_NODE,
                    node_name='#text',
                    owner_document=document,
                    node_value='foo',
                    read_only=False)
        self.assertEqual(text.node_value, 'foo')

    def testSetter(self):
        document = _create_document_node()
        text = Node(node_type=NodeType.TEXT_NODE,
                    node_name='#text',
                    owner_document=document,
                    read_only=False)
        text.node_value = 'bar'
        self.assertEqual(text.node_value, 'bar')

    def testSetter_ReadOnly(self):
        document = _create_document_node()
        text = Node(node_type=NodeType.TEXT_NODE,
                    node_name='#text',
                    owner_document=document,
                    node_value='foo',
                    read_only=True)
        try:
            text.node_value = 'bar'
        except DOMException as e:
            code = e.args[0]
            self.assertEqual(code, DOMException.NO_MODIFICATION_ALLOWED_ERR)
        else:
            self.fail()
        # `node_value` should not be modified.
        self.assertEqual(text.node_value, 'foo')


class Test_NodeType(unittest.TestCase):
    def testGetter(self):
        document = _create_document_node()
        for node_type in NodeType:
            node = Node(node_type=node_type,
                        node_name='',
                        owner_document=document)
            self.assertEqual(node.node_type, node_type)

    def testSetter_CorrectTypes(self):
        document = _create_document_node()
        for node_type in NodeType:
            Node(node_type=node_type,
                 node_name='',
                 owner_document=document)

    def testSetter_WrongTypes(self):
        document = _create_document_node()
        for node_type in [-1, None, 'hi', True, Node, NodeType, 'DOCUMENT_NODE']:
            try:
                Node(node_type=node_type,
                     node_name='',
                     owner_document=document)
                self.fail()
            except Exception:
                pass


class Test_ParentNode(unittest.TestCase):
    def testConstrutor(self):
        document = _create_document_node()
        docfrag = Node(node_type=NodeType.DOCUMENT_FRAGMENT_NODE,
                       node_name='#document-fragment',
                       owner_document=document)
        self.assertIsNone(docfrag.parent_node)

    def testGetter(self):
        document = _create_document_node()
        parent_node = _create_element_node(document)
        child_node = _create_element_node(document)
        # Warning: this is assuming that `append_child()` method works properly.
        parent_node.append_child(child_node)
        self.assertEqual(child_node.parent_node, parent_node)

    def testSetter_Raises_Exception(self):
        document = _create_document_node()
        parent_node = _create_element_node(document)
        child_node = _create_element_node(document)
        try:
            child_node.parent_node = parent_node
        except:
            self.assertNotEqual(child_node.parent_node, parent_node)
        else:
            self.fail()

class Test_InsertBefore(unittest.TestCase):
    def test_WithoutRefNode(self):
        document = _create_document_node()
        parent_node = _create_element_node(document)
        child_node = _create_element_node(document)
        # Testing
        parent_node.insert_before(child_node)
        self.assertEqual(child_node.parent_node, parent_node)
        self.assertEqual(parent_node.child_nodes.item(0), child_node)
        self.assertEqual(parent_node.child_nodes.length, 1)

    def test_WithRefNode(self):
        document = _create_document_node()
        parent_node = _create_element_node(document)
        first_child_node = _create_element_node(document)
        second_child_node = _create_element_node(document)
        # Warning: this is assuming that `append_child()` method works properly.
        parent_node.append_child(second_child_node)
        # Testing
        parent_node.insert_before(first_child_node, second_child_node)
        self.assertEqual(first_child_node.parent_node, parent_node)
        self.assertEqual(parent_node.child_nodes.item(0), first_child_node)
        self.assertEqual(parent_node.child_nodes.item(1), second_child_node)
        self.assertEqual(parent_node.child_nodes.length, 2)

    def test_InsertExistingChild(self):
        document = _create_document_node()
        parent_node = _create_element_node(document)
        first_child_node = _create_element_node(document)
        second_child_node = _create_element_node(document)
        # Warning: this is assuming that `append_child()` method works properly.
        parent_node.append_child(first_child_node)
        parent_node.append_child(second_child_node)
        # Testing
        parent_node.insert_before(second_child_node, first_child_node)
        self.assertEqual(second_child_node.parent_node, parent_node)
        self.assertEqual(parent_node.child_nodes.item(0), second_child_node)
        self.assertEqual(parent_node.child_nodes.item(1), first_child_node)
        self.assertEqual(parent_node.child_nodes.length, 2)

    def test_InsertDocumentFragmentNode(self):
        document = _create_document_node()
        parent_node = _create_element_node(document)
        docfrag_node = Node(node_type=NodeType.DOCUMENT_FRAGMENT_NODE,
                            node_name='#document-fragment',
                            owner_document=document)
        first_child_node = _create_element_node(document)
        second_child_node = _create_element_node(document)
        # Warning: this is assuming that `append_child()` method works properly.
        docfrag_node.append_child(first_child_node)
        docfrag_node.append_child(second_child_node)
        # Testing
        parent_node.insert_before(docfrag_node)
        self.assertEqual(parent_node.child_nodes.item(0), first_child_node)
        self.assertEqual(parent_node.child_nodes.item(1), second_child_node)
        self.assertEqual(parent_node.child_nodes.length, 2)

    def test_Raises_HIERARCHY_REQUEST_ERR(self):
        self.skipTest(NotImplemented)  # TODO

    def test_Raises_WRONG_DOCUMENT_ERR(self):
        document_1 = _create_document_node()
        document_2 = _create_document_node()
        elem_node_1 = _create_element_node(document_1)
        elem_node_2 = _create_element_node(document_2)
        try:
            elem_node_1.insert_before(elem_node_2)
        except DOMException as e:
            code = e.args[0]
            self.assertEqual(code, DOMException.WRONG_DOCUMENT_ERR)
        else:
            self.fail()

    def test_Raises_NO_MODIFICATION_ALLOWED_ERR(self):
        document = _create_document_node()
        elem_node_readonly = Node(node_type=NodeType.ELEMENT_NODE,
                                  node_name='tagName',
                                  owner_document=document,
                                  read_only=True)
        elem_node_child = _create_element_node(document)
        try:
            elem_node_readonly.insert_before(elem_node_child)
        except DOMException as e:
            code = e.args[0]
            self.assertEqual(code, DOMException.NO_MODIFICATION_ALLOWED_ERR)
        else:
            self.fail()

    def test_Raises_NOT_FOUND_ERR(self):
        document = _create_document_node()
        elem_node_parent = _create_element_node(document)
        elem_node_child = _create_element_node(document)
        elem_node_error = _create_element_node(document)
        # Testing
        try:
            elem_node_parent.insert_before(elem_node_child, elem_node_error)
        except DOMException as e:
            code = e.args[0]
            self.assertEqual(code, DOMException.NOT_FOUND_ERR)
        else:
            self.fail()


if __name__ == '__main__':
    unittest.main()
