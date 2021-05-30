from __future__ import absolute_import

import enum
import warnings
from typing import Optional

from python.dom.core.interface.fundamental.DOMException import DOMException
from python.dom.core.interface.fundamental.NamedNodeMap import NamedNodeMap
from python.dom.core.interface.fundamental.NodeList import NodeList
from python.dom.core.type import AnyNode
from python.dom.core.type import Document
from python.dom.core.type import DOMString


class NodeType(enum.IntEnum):
    """Definition group `NodeType`

    An integer indicating which type of node this is.
    """
    ELEMENT_NODE = 1  # The node is a `Element`.
    ATTRIBUTE_NODE = 2  # The node is an `Attr`.
    TEXT_NODE = 3  # The node is a `Text` node.
    CDATA_SECTION_NODE = 4  # The node is a `CDATASection`.
    ENTITY_REFERENCE_NODE = 5  # The node is an `EntityReference`.
    ENTITY_NODE = 6  # The node is an `Entity`.
    PROCESSING_INSTRUCTION_NODE = 7  # The node is a `ProcessingInstruction`.
    COMMENT_NODE = 8  # The node is a `Comment`.
    DOCUMENT_NODE = 9  # The node is a `Document`.
    DOCUMENT_TYPE_NODE = 10  # The node is a `DocumentType`.
    DOCUMENT_FRAGMENT_NODE = 11  # The node is a `DocumentFragment`.
    NOTATION_NODE = 12  # The node is a `Notation`.


class Node:
    """Interface `Node`

    The `Node` interface is the primary datatype for the entire Document Object Model. It represents a single node in the document tree. While all objects implementing the `Node` interface expose methods for dealing with children, not all objects implementing the `Node` interface may have children. For example, `Text` nodes may not have children, and adding children to such nodes results in a `DOMException` being raised.

    The attributes `node_name`, `node_value` and attributes are included as a mechanism to get at node information without casting down to the specific derived interface. In cases where there is no obvious mapping of these attributes for a specific `node_type` (e.g., `node_value` for an Element or `attributes` for a Comment), this returns `None`. Note that the specialized interfaces may contain additional and more convenient mechanisms to get and set the relevant information.
    """

    def __init__(self,
                 owner_document: Document,
                 node_type: NodeType,
                 parent_node: Optional[AnyNode] = None,
                 read_only: bool = False) -> None:
        self._set_parent_node(parent_node, node_type)
        self._node_type: NodeType = node_type
        self._read_only: bool = read_only
        # parent node should be set with `_set_parent_node` method.
        self._parent_node: Optional[AnyNode]
        self._child_nodes: NodeList = NodeList()
        self._previous_sibling: Optional[AnyNode] = None
        self._next_sibling: Optional[AnyNode] = None
        self._owner_document: Document = owner_document

    @property
    def node_name(self) -> DOMString:
        """The name of this node, depending on its type.
        """
        raise NotImplementedError

    @property
    def node_value(self) -> DOMString:
        """The value of this node, depending on its type.

        Raises:
            DOMException:
            - `NO_MODIFICATION_ALLOWED_ERR`: Raised when the node is readonly. (on setting)
            - `DOMSTRING_SIZE_ERR`: Raised when it would return more characters than fit in a `DOMString` variable on the implementation platform. (on retrieval)
        """
        raise NotImplementedError

    @node_value.setter
    def node_value(self, value: DOMString) -> None:
        if self._read_only:
            raise DOMException(DOMException.NO_MODIFICATION_ALLOWED_ERR)
        raise NotImplementedError

    @property
    def node_type(self) -> NodeType:
        """A code representing the type of the underlying object.
        """
        return self._node_type

    @property
    def parent_node(self) -> Optional[AnyNode]:
        """The parent of this node. All nodes, except `Document`, `DocumentFragment`, and `Attr` may have a parent. However, if a node has just been created and not yet added to the tree, or if it has been removed from the tree, this is null.
        """
        return self._parent_node

    def _set_parent_node(self,
                         parent_node: Optional[AnyNode],
                         node_type: Optional[NodeType] = None) -> None:
        """Sets parent node of this node. If given `parent_node` is a node that cannot have its parent, this method will raise a warning.

        Args:
            parent_node: A node which is the parent of this node.
            node_type: Optional; Value to be assumed as the type of this node. If `node_type` is not given, it will be replaced with the type of this node.
        """
        if node_type is None:
            node_type = self.node_type
        if parent_node is not None:
            if self.node_type in [NodeType.DOCUMENT_NODE,
                                  NodeType.DOCUMENT_FRAGMENT_NODE,
                                  NodeType.ATTRIBUTE_NODE]:
                warnings.warn('Document, DocumentFragment, '
                              'and Attr may not have a parent.')
        self._parent_node = parent_node

    @property
    def child_nodes(self) -> NodeList:
        """A `NodeList` that contains all children of this node. If there are no children, this is a `NodeList` containing no nodes. The content of the returned `NodeList` is "live" in the sense that, for instance, changes to the children of the node object that it was created from are immediately reflected in the nodes returned by the `NodeList` accessors; it is not a static snapshot of the content of the node. This is true for every `NodeList`, including the ones returned by the `getElementsByTagName` method.
        """
        return self._child_nodes

    @property
    def first_child(self) -> Optional[AnyNode]:
        """The first child of this node. If there is no such node, this returns `None`.
        """
        if not self.child_nodes:
            return None
        else:
            return self.child_nodes.item(0)

    @property
    def last_child(self) -> Optional[AnyNode]:
        """The last child of this node. If there is no such node, this returns `None`.
        """
        if not self.child_nodes:
            return None
        else:
            return self.child_nodes.item(self.child_nodes.length-1)

    @property
    def previous_sibling(self) -> Optional[AnyNode]:
        """The node immediately preceding this node. If there is no such node, this returns `None`.
        """
        return self._previous_sibling

    @property
    def next_sibling(self) -> Optional[AnyNode]:
        """The node immediately following this node. If there is no such node, this returns `None`.
        """
        return self._next_sibling

    @property
    def attributes(self) -> Optional[NamedNodeMap]:
        """A `NamedNodeMap` containing the attributes of this node (if it is an `Element`) or `None` otherwise.
        """
        raise NotImplementedError

    @property
    def owner_document(self) -> Optional[Document]:
        """The `Document` object associated with this node. This is also the `Document` object used to create new nodes. When this node is a `Document` this is `None`.
        """
        return self._owner_document

    def _is_allowed_child_type(self, new_child: AnyNode) -> bool:
        """Whether a node can be the child of this node.
        (only checks with the type of nodes.)

        Args:
            new_child: The node to check insertable.

        Returns:
            Boolean that indicates if the `new_child` is an allowed type.
        """
        # TODO: Make this method abstract.
        if new_child.node_type == NodeType.DOCUMENT_FRAGMENT_NODE:
            for child in new_child.child_nodes:
                if not self._is_allowed_child_type(child):
                    return False
            return True
        if self.node_type == NodeType.DOCUMENT_NODE:
            if new_child.node_type == NodeType.ELEMENT_NODE:
                for child in self.child_nodes:
                    if child.node_type == NodeType.ELEMENT_NODE:
                        return False
                return True
            elif new_child.node_type in [NodeType.PROCESSING_INSTRUCTION_NODE,
                                         NodeType.COMMENT_NODE,
                                         NodeType.DOCUMENT_TYPE_NODE]:
                return True
            else:
                return False
        elif self.node_type == NodeType.DOCUMENT_FRAGMENT_NODE:
            if new_child.node_type in [NodeType.ELEMENT_NODE,
                                       NodeType.PROCESSING_INSTRUCTION_NODE,
                                       NodeType.COMMENT_NODE,
                                       NodeType.TEXT_NODE,
                                       NodeType.CDATA_SECTION_NODE,
                                       NodeType.ENTITY_REFERENCE_NODE]:
                return True
            else:
                return False
        elif self.node_type == NodeType.DOCUMENT_TYPE_NODE:
            return False
        elif self.node_type == NodeType.ENTITY_REFERENCE_NODE:
            if new_child.node_type in [NodeType.ELEMENT_NODE,
                                       NodeType.PROCESSING_INSTRUCTION_NODE,
                                       NodeType.COMMENT_NODE,
                                       NodeType.TEXT_NODE,
                                       NodeType.CDATA_SECTION_NODE,
                                       NodeType.ENTITY_REFERENCE_NODE]:
                return True
            else:
                return False
        elif self.node_type == NodeType.ELEMENT_NODE:
            if new_child.node_type in [NodeType.ELEMENT_NODE,
                                       NodeType.TEXT_NODE,
                                       NodeType.COMMENT_NODE,
                                       NodeType.PROCESSING_INSTRUCTION_NODE,
                                       NodeType.CDATA_SECTION_NODE,
                                       NodeType.ENTITY_REFERENCE_NODE]:
                return True
            else:
                return False
        elif self.node_type == NodeType.ATTRIBUTE_NODE:
            if new_child.node_type in [NodeType.TEXT_NODE,
                                       NodeType.ENTITY_REFERENCE_NODE]:
                return True
            else:
                return False
        elif self.node_type == NodeType.ENTITY_NODE:
            if new_child.node_type in [NodeType.ELEMENT_NODE,
                                       NodeType.PROCESSING_INSTRUCTION_NODE,
                                       NodeType.COMMENT_NODE,
                                       NodeType.TEXT_NODE,
                                       NodeType.CDATA_SECTION_NODE,
                                       NodeType.ENTITY_REFERENCE_NODE]:
                return True
            else:
                return False
        else:
            return False

    def _check_insertable(self, new_child: AnyNode) -> None:
        """Whether a node can be the child of this node. Raises `DOMException` if the given node is not insertable.

        Args:
            new_child: The node to check insertable.

        Returns:
            This method does not return any value.

        Raises:
            DOMException:
            - `HIERARCHY_REQUEST_ERR`: Raised if this node is of a type that does not allow children of the type of the `new_child` node, or if the node to insert is one of this node's ancestors.
            - `WRONG_DOCUMENT_ERR`: Raised if `new_child` was created from a different document than the one that created this node.
            - `NO_MODIFICATION_ALLOWED_ERR`: Raised if this node is readonly.
        """
        if self._read_only:
            raise DOMException(DOMException.NO_MODIFICATION_ALLOWED_ERR)
        if new_child.owner_document is not self.owner_document:
            raise DOMException(DOMException.WRONG_DOCUMENT_ERR)
        if not self._is_allowed_child_type(new_child):
            raise DOMException(DOMException.HIERARCHY_REQUEST_ERR)

    def insert_before(self,
                      new_child: AnyNode,
                      ref_child: Optional[AnyNode] = None) -> AnyNode:
        """Inserts the node `new_child` before the existing child node `ref_child`. If `ref_child` is `None`, insert `new_child` at the end of the list of children.

        If `new_child` is a `DocumentFragment` object, all of its children are inserted, in the same order, before `ref_child`. If the `new_child` is already in the tree, it is first removed.

        Args:
            new_child: The node to insert.
            ref_child: The reference node, i.e., the node before which the new node must be inserted.

        Returns:
            The node being inserted.

        Raises:
            DOMException:
            - `HIERARCHY_REQUEST_ERR`: Raised if this node is of a type that does not allow children of the type of the `new_child` node, or if the node to insert is one of this node's ancestors.
            - `WRONG_DOCUMENT_ERR`: Raised if `new_child` was created from a different document than the one that created this node.
            - `NO_MODIFICATION_ALLOWED_ERR`: Raised if this node is readonly.
            - `NOT_FOUND_ERR`: Raised if `ref_child` is not a child of this node.
        """
        self._check_insertable(new_child)
        # If `new_child` is a `DocumentFragment` object, all of its children are inserted
        if new_child.node_type == Node.DOCUMENT_FRAGMENT_NODE:
            for child in new_child.child_nodes:
                self.insert_before(child, ref_child)
            return new_child
        # If the `new_child` is already in the tree, it is first removed.
        if new_child in self.child_nodes:
            self.child_nodes.remove(new_child)
        # If `ref_child` is `None`, insert `new_child` at the end of the list of children.
        if ref_child is None:
            self.child_nodes.append(new_child)
        elif ref_child in self.child_nodes:
            ref_index = self.child_nodes.index(ref_child)
            self.child_nodes.insert(ref_index, new_child)
        else:
            raise DOMException(DOMException.NOT_FOUND_ERR)
        # Bind `new_child` to this node.
        new_child._set_parent_node(self)
        return new_child
