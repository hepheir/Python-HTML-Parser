from __future__ import absolute_import
from __future__ import annotations

import unittest

from python.dom.DOMException import DOMException
from python.dom.node import Node, Document


class Test_Node(unittest.TestCase):
    def testInsertBefore_withoutRefNode(self):
        document = Document()
        parent_node = Node(document, Node.ELEMENT_NODE)
        child_node = Node(document, Node.ELEMENT_NODE)
        # Testing
        parent_node.insert_before(child_node)
        self.assertEqual(child_node.parent_node, parent_node)
        self.assertEqual(parent_node.child_nodes.item(0), child_node)
        self.assertEqual(parent_node.child_nodes.length, 1)

    def testInsertBefore_withRefNode(self):
        document = Document()
        parent_node = Node(document, Node.ELEMENT_NODE)
        first_child_node = Node(document, Node.ELEMENT_NODE)
        second_child_node = Node(document, Node.ELEMENT_NODE)
        # Following task should've been tested via `testInsertBefore_withoutRefNode()`.
        parent_node.insert_before(second_child_node)
        # Testing
        parent_node.insert_before(first_child_node, second_child_node)
        self.assertEqual(first_child_node.parent_node, parent_node)
        self.assertEqual(parent_node.child_nodes.item(0), first_child_node)
        self.assertEqual(parent_node.child_nodes.item(1), second_child_node)
        self.assertEqual(parent_node.child_nodes.length, 2)

    def testInsertBefore_insertExistingChild(self):
        document = Document()
        parent_node = Node(document, Node.ELEMENT_NODE)
        first_child_node = Node(document, Node.ELEMENT_NODE)
        second_child_node = Node(document, Node.ELEMENT_NODE)
        # Following tasks should've been tested via `testInsertBefore_withoutRefNode()`.
        parent_node.insert_before(first_child_node)
        parent_node.insert_before(second_child_node)
        # Testing
        parent_node.insert_before(second_child_node, first_child_node)
        self.assertEqual(second_child_node.parent_node, parent_node)
        self.assertEqual(parent_node.child_nodes.item(0), second_child_node)
        self.assertEqual(parent_node.child_nodes.item(1), first_child_node)
        self.assertEqual(parent_node.child_nodes.length, 2)

    def testInsertBefore_insertDocumentFragmentNode(self):
        document = Document()
        parent_node = Node(document, Node.ELEMENT_NODE)
        df_node = Node(document, Node.DOCUMENT_FRAGMENT_NODE)
        first_child_node = Node(document, Node.ELEMENT_NODE)
        second_child_node = Node(document, Node.ELEMENT_NODE)
        # Following tasks should've been tested via `testInsertBefore_withoutRefNode()`.
        df_node.insert_before(first_child_node)
        df_node.insert_before(second_child_node)
        # Testing
        parent_node.insert_before(df_node)
        self.assertEqual(parent_node.child_nodes.item(0), first_child_node)
        self.assertEqual(parent_node.child_nodes.item(1), second_child_node)
        self.assertEqual(parent_node.child_nodes.length, 2)

    def testInsertBefore_raises_HIERARCHY_REQUEST_ERR(self):
        document = Document()
        parent_node = Node(document, Node.ATTRIBUTE_NODE)
        child_node = Node(document, Node.TEXT_NODE)
        child_node_not_allowed = Node(document, Node.ELEMENT_NODE)
        # Following task should've been tested via `testInsertBefore_withoutRefNode()`.
        parent_node.insert_before(child_node)
        # Testing: Not allowed type of child node.
        try:
            parent_node.insert_before(child_node_not_allowed)
        except DOMException as e:
            code = e.args[0]
            self.assertEqual(code, DOMException.HIERARCHY_REQUEST_ERR)
        else:
            self.fail()
        # Testing: Try to insert own ancestor as a child node.
        try:
            child_node.insert_before(parent_node)
        except DOMException as e:
            code = e.args[0]
            self.assertEqual(code, DOMException.HIERARCHY_REQUEST_ERR)
        else:
            self.fail()

    def testInsertBefore_raises_WRONG_DOCUMENT_ERR(self):
        document_1 = Document()
        document_2 = Document()
        parent_node = Node(document_1, Node.ELEMENT_NODE)
        child_node = Node(document_2, Node.ELEMENT_NODE)
        try:
            parent_node.insert_before(child_node)
        except DOMException as e:
            code = e.args[0]
            self.assertEqual(code, DOMException.WRONG_DOCUMENT_ERR)
        else:
            self.fail()

    def testInsertBefore_raises_NO_MODIFICATION_ALLOWED_ERR(self):
        document = Document()
        readonly_node = Node(document, Node.ELEMENT_NODE, read_only=True)
        child_node = Node(document, Node.ELEMENT_NODE)
        try:
            readonly_node.insert_before(child_node)
        except DOMException as e:
            code = e.args[0]
            self.assertEqual(code, DOMException.NO_MODIFICATION_ALLOWED_ERR)
        else:
            self.fail()

    def testInsertBefore_raises_NOT_FOUND_ERR(self):
        document = Document()
        parent_node = Node(document, Node.ELEMENT_NODE)
        child_node = Node(document, Node.ELEMENT_NODE)
        wrong_ref_node = Node(document, Node.ELEMENT_NODE)
        # Testing
        try:
            parent_node.insert_before(child_node, wrong_ref_node)
        except DOMException as e:
            code = e.args[0]
            self.assertEqual(code, DOMException.NOT_FOUND_ERR)
        else:
            self.fail()
