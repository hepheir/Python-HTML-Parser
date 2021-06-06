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


class TestDunder_Init(unittest.TestCase):
    def test_Default(self):
        # Creating document node.
        document = Node(node_type=NodeType.DOCUMENT_NODE,
                        node_name='#document',
                        owner_document=None,
                        read_only=False)
        self.assertEqual(document.node_type, NodeType.DOCUMENT_NODE)
        self.assertEqual(document.node_name, '#document')
        self.assertEqual(document.node_value, '')


class TestProperty_NodeValue(unittest.TestCase):
    def setUp(self) -> None:
        self.document = _create_document_node()
        return super().setUp()

    def testGetter(self):
        text = Node(node_type=NodeType.TEXT_NODE,
                    node_name='#text',
                    owner_document=self.document,
                    node_value='lorem ipsum')
        self.assertEqual(text.node_value, 'lorem ipsum')

    def testConstructor(self):
        text = Node(node_type=NodeType.TEXT_NODE,
                    node_name='#text',
                    owner_document=self.document,
                    node_value='foo',
                    read_only=False)
        self.assertEqual(text.node_value, 'foo')

    def testSetter(self):
        text = Node(node_type=NodeType.TEXT_NODE,
                    node_name='#text',
                    owner_document=self.document,
                    read_only=False)
        text.node_value = 'bar'
        self.assertEqual(text.node_value, 'bar')

    def testSetter_ReadOnly(self):
        text = Node(node_type=NodeType.TEXT_NODE,
                    node_name='#text',
                    owner_document=self.document,
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


class TestProperty_NodeType(unittest.TestCase):
    def setUp(self) -> None:
        self.document = _create_document_node()
        return super().setUp()

    def testGetter(self):
        for node_type in NodeType:
            node = Node(node_type=node_type,
                        node_name='',
                        owner_document=self.document)
            self.assertEqual(node.node_type, node_type)

    def testSetter_CorrectTypes(self):
        for node_type in NodeType:
            with self.subTest(node_type=node_type):
                Node(node_type=node_type,
                     node_name='',
                     owner_document=self.document)

    def testSetter_WrongTypes(self):
        for node_type in [-1, None, 'hi', True, Node, NodeType, 'DOCUMENT_NODE']:
            with self.subTest(node_type=node_type):
                try:
                    Node(node_type=node_type,
                         node_name='',
                         owner_document=self.document)
                except Exception:
                    pass
                else:
                    self.fail()


class TestProperty_ParentNode(unittest.TestCase):
    def setUp(self) -> None:
        self.document = _create_document_node()
        return super().setUp()

    def testConstrutor(self):
        docfrag = Node(node_type=NodeType.DOCUMENT_FRAGMENT_NODE,
                       node_name='#document-fragment',
                       owner_document=self.document)
        self.assertIsNone(docfrag.parent_node)

    def testGetter(self):
        parent_node = _create_element_node(self.document)
        child_node = _create_element_node(self.document)
        # Warning: this is assuming that `append_child()` method works properly.
        parent_node.append_child(child_node)
        self.assertEqual(child_node.parent_node, parent_node)

    def testSetter_Raises_Exception(self):
        parent_node = _create_element_node(self.document)
        child_node = _create_element_node(self.document)
        try:
            child_node.parent_node = parent_node  # type: ignore
        except:
            self.assertNotEqual(child_node.parent_node, parent_node)
        else:
            self.fail()


class TestMethod_InsertBefore(unittest.TestCase):
    def setUp(self) -> None:
        self.document = _create_document_node()
        return super().setUp()

    def test_WithoutRefNode(self):
        # ======================================
        # <document>
        #     <parent_node/>
        #     <new_child_node/>
        # <document>
        # ======================================
        parent_node = _create_element_node(self.document)
        new_child_node = _create_element_node(self.document)
        # Testing
        parent_node.insert_before(new_child_node)
        self.assertEqual(new_child_node.parent_node, parent_node)
        self.assertEqual(parent_node.child_nodes.item(0), new_child_node)
        self.assertEqual(parent_node.child_nodes.length, 1)

    def test_WithRefNode(self):
        # ======================================
        # <document>
        #     <parent_node>
        #         <ref_child_node/>
        #     </parent_node>
        #
        #     <new_child_node/>
        # <document>
        # ======================================
        parent_node = _create_element_node(self.document)
        new_child_node = _create_element_node(self.document)
        ref_child_node = _create_element_node(self.document)
        parent_node.append_child(ref_child_node)
        # Testing
        parent_node.insert_before(new_child_node, ref_child_node)
        self.assertEqual(new_child_node.parent_node, parent_node)
        self.assertEqual(parent_node.child_nodes.item(0), new_child_node)
        self.assertEqual(parent_node.child_nodes.item(1), ref_child_node)
        self.assertEqual(parent_node.child_nodes.length, 2)

    def test_InsertExistingChild(self):
        # ======================================
        # <document>
        #     <parent_node>
        #         <ref_child_node/>
        #         <new_child_node/>
        #     </parent_node>
        # <document>
        # ======================================
        parent_node = _create_element_node(self.document)
        ref_child_node = _create_element_node(self.document)
        new_child_node = _create_element_node(self.document)
        parent_node.append_child(ref_child_node)
        parent_node.append_child(new_child_node)
        # Testing
        parent_node.insert_before(new_child_node, ref_child_node)
        self.assertEqual(new_child_node.parent_node, parent_node)
        self.assertEqual(parent_node.child_nodes.item(0), new_child_node)
        self.assertEqual(parent_node.child_nodes.item(1), ref_child_node)
        self.assertEqual(parent_node.child_nodes.length, 2)

    def test_InsertDocumentFragmentNode(self):
        # ======================================
        # <document>
        #     <parent_node/>
        #
        #     <docfrag_node>
        #         <first_child_node/>
        #         <second_child_node/>
        #     </docfrag_node>
        # <document>
        # ======================================
        parent_node = _create_element_node(self.document)
        docfrag_node = Node(node_type=NodeType.DOCUMENT_FRAGMENT_NODE,
                            node_name='#document-fragment',
                            owner_document=self.document)
        first_child_node = _create_element_node(self.document)
        second_child_node = _create_element_node(self.document)
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
        # ======================================
        # <document1>
        #     <elem_node_1/>
        # <document1>
        #
        # <document2>
        #     <elem_node_2/>
        # <document2>
        # ======================================
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
        # ======================================
        # <document>
        #     <parent_node readonly="true"/>
        #     <new_child_node/>
        # <document>
        # ======================================
        parent_node_readonly = Node(node_type=NodeType.ELEMENT_NODE,
                                    node_name='tagName',
                                    owner_document=self.document,
                                    read_only=True)
        new_child_node = _create_element_node(self.document)
        try:
            parent_node_readonly.insert_before(new_child_node)
        except DOMException as e:
            code = e.args[0]
            self.assertEqual(code, DOMException.NO_MODIFICATION_ALLOWED_ERR)
        else:
            self.fail()

    def test_Raises_NOT_FOUND_ERR(self):
        # ======================================
        # <document>
        #     <parent_node/>
        #     <new_child_node/>
        #     <ref_child_node/>
        # <document>
        # ======================================
        parent_node = _create_element_node(self.document)
        new_child_node = _create_element_node(self.document)
        ref_child_node = _create_element_node(self.document)
        # Testing
        try:
            parent_node.insert_before(new_child_node, ref_child_node)
        except DOMException as e:
            code = e.args[0]
            self.assertEqual(code, DOMException.NOT_FOUND_ERR)
        else:
            self.fail()


class TestMethod_AppendChild(unittest.TestCase):
    def setUp(self) -> None:
        self.document = _create_document_node()
        return super().setUp()

    def test_AppendNewChild(self):
        # ======================================
        # <document>
        #     <parent_node/>
        #     <new_child_node/>
        # <document>
        # ======================================
        parent_node = _create_element_node(self.document)
        new_child_node = _create_element_node(self.document)
        # Testing
        parent_node.append_child(new_child_node)
        self.assertEqual(new_child_node.parent_node, parent_node)
        self.assertEqual(parent_node.child_nodes.item(0), new_child_node)
        self.assertEqual(parent_node.child_nodes.length, 1)

    def test_AppendExistingChild(self):
        # ======================================
        # <document>
        #     <parent_node>
        #         <new_child_node/>
        #         <old_child_node/>
        #     </parent_node>
        # <document>
        # ======================================
        parent_node = _create_element_node(self.document)
        new_child_node = _create_element_node(self.document)
        old_child_node = _create_element_node(self.document)
        parent_node.append_child(new_child_node)
        parent_node.append_child(old_child_node)
        # Testing
        parent_node.append_child(new_child_node)
        self.assertEqual(old_child_node.parent_node, parent_node)
        self.assertEqual(parent_node.child_nodes.item(0), old_child_node)
        self.assertEqual(parent_node.child_nodes.item(1), new_child_node)
        self.assertEqual(parent_node.child_nodes.length, 2)

    def test_AppendDocumentFragmentNode(self):
        # ======================================
        # <document>
        #     <parent_node/>
        #
        #     <docfrag_node>
        #         <first_child_node/>
        #         <second_child_node/>
        #     </docfrag_node>
        # <document>
        # ======================================
        parent_node = _create_element_node(self.document)
        docfrag_node = Node(node_type=NodeType.DOCUMENT_FRAGMENT_NODE,
                            node_name='#document-fragment',
                            owner_document=self.document)
        first_child_node = _create_element_node(self.document)
        second_child_node = _create_element_node(self.document)
        docfrag_node.append_child(first_child_node)
        docfrag_node.append_child(second_child_node)
        # Testing
        parent_node.append_child(docfrag_node)
        self.assertEqual(parent_node.child_nodes.item(0), first_child_node)
        self.assertEqual(parent_node.child_nodes.item(1), second_child_node)
        self.assertEqual(parent_node.child_nodes.length, 2)

    def test_Raises_HIERARCHY_REQUEST_ERR(self):
        self.skipTest(NotImplemented)  # TODO

    def test_Raises_WRONG_DOCUMENT_ERR(self):
        # ======================================
        # <document1>
        #     <elem_node_1/>
        # <document1>
        #
        # <document2>
        #     <elem_node_2/>
        # <document2>
        # ======================================
        document_1 = _create_document_node()
        document_2 = _create_document_node()
        elem_node_1 = _create_element_node(document_1)
        elem_node_2 = _create_element_node(document_2)
        try:
            elem_node_1.append_child(elem_node_2)
        except DOMException as e:
            code = e.args[0]
            self.assertEqual(code, DOMException.WRONG_DOCUMENT_ERR)
        else:
            self.fail()

    def test_Raises_NO_MODIFICATION_ALLOWED_ERR(self):
        # ======================================
        # <document>
        #     <parent_node readonly="true"/>
        #     <new_child_node/>
        # <document>
        # ======================================
        parent_node_readonly = Node(node_type=NodeType.ELEMENT_NODE,
                                    node_name='tagName',
                                    owner_document=self.document,
                                    read_only=True)
        new_child_node = _create_element_node(self.document)
        try:
            parent_node_readonly.append_child(new_child_node)
        except DOMException as e:
            code = e.args[0]
            self.assertEqual(code, DOMException.NO_MODIFICATION_ALLOWED_ERR)
        else:
            self.fail()


class TestMethod_ReplaceChild(unittest.TestCase):
    def setUp(self) -> None:
        self.document = _create_document_node()
        return super().setUp()

    def test_ReplaceExistingChild(self):
        # ======================================
        # <document>
        #     <parent_node>
        #         <old_child_node/>
        #     </parent_node>
        #
        #     <new_child_node/>
        # <document>
        # ======================================
        parent_node = _create_element_node(self.document)
        new_child_node = _create_element_node(self.document)
        old_child_node = _create_element_node(self.document)
        parent_node.append_child(old_child_node)
        # Testing
        parent_node.replace_child(new_child_node, old_child_node)
        self.assertIn(new_child_node, parent_node.child_nodes)
        self.assertNotIn(old_child_node, parent_node.child_nodes)
        self.assertEqual(new_child_node.parent_node, parent_node)
        self.assertEqual(parent_node.child_nodes.item(0), new_child_node)
        self.assertEqual(parent_node.child_nodes.length, 1)

    def test_Raises_HIERARCHY_REQUEST_ERR(self):
        self.skipTest(NotImplemented)  # TODO

    def test_Raises_WRONG_DOCUMENT_ERR(self):
        # ======================================
        # <document1>
        #     <parent_node>
        #         <old_child_node/>
        #     </parent_node>
        # <document1>
        #
        # <document2>
        #     <new_child_node/>
        # <document2>
        # ======================================
        document_1 = _create_document_node()
        document_2 = _create_document_node()
        parent_node = _create_element_node(document_1)
        old_child_node = _create_element_node(document_1)
        new_child_node = _create_element_node(document_2)
        parent_node.append_child(old_child_node)
        try:
            parent_node.replace_child(new_child_node, old_child_node)
        except DOMException as e:
            code = e.args[0]
            self.assertEqual(code, DOMException.WRONG_DOCUMENT_ERR)
        else:
            self.fail()

    def test_Raises_NO_MODIFICATION_ALLOWED_ERR(self):
        # ======================================
        # <document>
        #     <parent_node readonly="true"/>
        #     <new_child_node/>
        # <document>
        # ======================================
        parent_node_readonly = Node(node_type=NodeType.ELEMENT_NODE,
                                    node_name='tagName',
                                    owner_document=self.document,
                                    read_only=True)
        new_child_node = _create_element_node(self.document)
        try:
            parent_node_readonly.append_child(new_child_node)
        except DOMException as e:
            code = e.args[0]
            self.assertEqual(code, DOMException.NO_MODIFICATION_ALLOWED_ERR)
        else:
            self.fail()


class TestMethod_HasChild(unittest.TestCase):
    def setUp(self) -> None:
        self.document = _create_document_node()
        return super().setUp()

    def test_True(self):
        # ======================================
        # <document>
        #     <parent_node>
        #         <child_node/>
        #     </parent_node>
        # <document>
        # ======================================
        parent_node = _create_element_node(self.document)
        child_node = _create_element_node(self.document)
        parent_node.append_child(child_node)
        # Testing
        self.assertTrue(parent_node.has_child_nodes())

    def test_False(self):
        # ======================================
        # <document>
        #     <node/>
        # <document>
        # ======================================
        node = _create_element_node(self.document)
        # Testing
        self.assertFalse(node.has_child_nodes())


class TestMethod_RemoveChild(unittest.TestCase):
    def setUp(self) -> None:
        self.document = _create_document_node()
        return super().setUp()

    def test_RemoveExistingChlid(self):
        # ======================================
        # <document>
        #     <parent_node>
        #         <child_node/>
        #     </parent_node>
        # <document>
        # ======================================
        parent_node = _create_element_node(self.document)
        child_node = _create_element_node(self.document)
        parent_node.append_child(child_node)
        # Testing
        parent_node.remove_child(child_node)
        self.assertNotIn(child_node, parent_node.child_nodes)
        self.assertIsNone(child_node.parent_node)

    def test_Raises_NOT_FOUND_ERR(self):
        # ======================================
        # <document>
        #     <parent_node/>
        #     <child_node/>
        # <document>
        # ======================================
        parent_node = _create_element_node(self.document)
        child_node = _create_element_node(self.document)
        # Testing
        try:
            parent_node.remove_child(child_node)
        except DOMException as de:
            self.assertEqual(de.args[0], DOMException.NOT_FOUND_ERR)
        else:
            self.fail()

    def test_Raises_NO_MODIFICATION_ALLOWED_ERR(self):
        # ======================================
        # <document>
        #     <parent_node read-only="true">
        #         <child_node/>
        #     </parent_node>
        # <document>
        # ======================================
        child_node = _create_element_node(self.document)
        parent_node = Node(node_type=NodeType.ELEMENT_NODE,
                           node_name='tagName',
                           owner_document=self.document,
                           child_nodes=[child_node],
                           read_only=True)
        # Testing
        try:
            parent_node.remove_child(child_node)
        except DOMException as de:
            code = de.args[0]
            self.assertEqual(code, DOMException.NO_MODIFICATION_ALLOWED_ERR)
        else:
            self.fail()


if __name__ == '__main__':
    unittest.main()
