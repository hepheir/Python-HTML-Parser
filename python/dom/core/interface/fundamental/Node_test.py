from __future__ import absolute_import

import unittest

from python.dom import Attr
from python.dom import Document
from python.dom import DocumentFragment
from python.dom import DOMException
from python.dom import Element
from python.dom import Text


class Test_Node(unittest.TestCase):
    def testInsertBefore_withoutRefNode(self):
        document = Document()
        parent_node = Element(document)
        child_node = Element(document)
        # Testing
        parent_node.insert_before(child_node)
        self.assertEqual(child_node.parent_node, parent_node)
        self.assertEqual(parent_node.child_nodes.item(0), child_node)
        self.assertEqual(parent_node.child_nodes.length, 1)

    def testInsertBefore_withRefNode(self):
        document = Document()
        parent_node = Element(document)
        first_child_node = Element(document)
        second_child_node = Element(document)
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
        parent_node = Element(document)
        first_child_node = Element(document)
        second_child_node = Element(document)
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
        parent_node = Element(document)
        df_node = DocumentFragment(document)
        first_child_node = Element(document)
        second_child_node = Element(document)
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
        parent_node = Attr(document)
        child_node = Text(document)
        child_node_not_allowed = Element(document)
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
        parent_node = Element(document_1)
        child_node = Element(document_2)
        try:
            parent_node.insert_before(child_node)
        except DOMException as e:
            code = e.args[0]
            self.assertEqual(code, DOMException.WRONG_DOCUMENT_ERR)
        else:
            self.fail()

    def testInsertBefore_raises_NO_MODIFICATION_ALLOWED_ERR(self):
        document = Document()
        readonly_node = Element(document, read_only=True)
        child_node = Element(document)
        try:
            readonly_node.insert_before(child_node)
        except DOMException as e:
            code = e.args[0]
            self.assertEqual(code, DOMException.NO_MODIFICATION_ALLOWED_ERR)
        else:
            self.fail()

    def testInsertBefore_raises_NOT_FOUND_ERR(self):
        document = Document()
        parent_node = Element(document)
        child_node = Element(document)
        wrong_ref_node = Element(document)
        # Testing
        try:
            parent_node.insert_before(child_node, wrong_ref_node)
        except DOMException as e:
            code = e.args[0]
            self.assertEqual(code, DOMException.NOT_FOUND_ERR)
        else:
            self.fail()
