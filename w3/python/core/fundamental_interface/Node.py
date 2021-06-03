from __future__ import annotations

import enum
from typing import Dict, Iterable, Optional

from w3.python.core.fundamental_interface.DOMException import DOMException
from w3.python.core.fundamental_interface.NodeList import NodeList
from w3.python.core.type import DOMString


class NodeType(enum.IntEnum):
    """Definition group `NodeType`

    An integer indicating which type of node this is.

    Attributes:
        ELEMENT_NODE: The node is a `Element`.
        ATTRIBUTE_NODE: The node is an `Attr`.
        TEXT_NODE: The node is a `Text` node.
        CDATA_SECTION_NODE: The node is a `CDATASection`.
        ENTITY_REFERENCE_NODE: The node is an `EntityReference`.
        ENTITY_NODE: The node is an `Entity`.
        PROCESSING_INSTRUCTION_NODE: The node is a `ProcessingInstruction`.
        COMMENT_NODE: The node is a `Comment`.
        DOCUMENT_NODE: The node is a `Document`.
        DOCUMENT_TYPE_NODE: The node is a `DocumentType`.
        DOCUMENT_FRAGMENT_NODE: The node is a `DocumentFragment`.
        NOTATION_NODE: The node is a `Notation`.
    """
    ELEMENT_NODE = 1
    ATTRIBUTE_NODE = 2
    TEXT_NODE = 3
    CDATA_SECTION_NODE = 4
    ENTITY_REFERENCE_NODE = 5
    ENTITY_NODE = 6
    PROCESSING_INSTRUCTION_NODE = 7
    COMMENT_NODE = 8
    DOCUMENT_NODE = 9
    DOCUMENT_TYPE_NODE = 10
    DOCUMENT_FRAGMENT_NODE = 11
    NOTATION_NODE = 12


class Node:
    """Interface `Node`

    The `Node` interface is the primary datatype for the entire Document Object Model. It represents a single node in the document tree. While all objects implementing the `Node` interface expose methods for dealing with children, not all objects implementing the `Node` interface may have children. For example, `Text` nodes may not have children, and adding children to such nodes results in a `DOMException` being raised.
    The attributes `node_name`, `node_value` and attributes are included as a mechanism to get at node information without casting down to the specific derived interface. In cases where there is no obvious mapping of these attributes for a specific `node_type` (e.g., `node_value` for an Element or `attributes` for a Comment), this returns `None`. Note that the specialized interfaces may contain additional and more convenient mechanisms to get and set the relevant information.

    Attributes:
        node_name: The name of this node, depending on its type.
        node_value: The value of this node, depending on its type.
        node_type: A code representing the type of the underlying object.
        parent_node: The parent of this node.
        child_nodes: A `NodeList` that contains all children of this node.
        first_child: The first child of this node.
        last_child: The last child of this node.
        previous_sibling: The node immediately preceding this node.
        next_sibling: The node immediately following this node.
        attributes: A `NamedNodeMap` containing the attributes of this node.
        owner_document: The `Document` object associated with this node.
    """

    def __init__(self,
                 node_type: NodeType,
                 node_name: DOMString,
                 node_value: Optional[DOMString] = None,
                 parent_node: Optional[_AnyNode] = None,
                 child_nodes: Optional[Iterable[_AnyNode]] = None,
                 attributes: Optional[Iterable[_AnyNode]] = None,
                 owner_document: Optional[_Document] = None,
                 read_only: bool = False) -> None:
        if node_value is None:
            node_value = ''
        self._read_only = False  # Allow to modify only while initiating.
        self._set_node_type(node_type)
        self._set_node_name(node_name)
        self._set_node_value(node_value)
        self._set_parent_node(parent_node)
        self._init_child_nodes(child_nodes)
        self._init_attributes(attributes)
        self._set_owner_document(owner_document)
        self._read_only = bool(read_only)
        # Attributes
        self._node_type: NodeType
        self._node_name: DOMString
        self._node_value: DOMString
        self._parent_node: _AnyNode
        self._child_nodes: NodeList
        self._attributes: _NamedNodeMap
        self._owner_document: _Document
        self._read_only: bool

    def _check_modifiable(self) -> None:
        """Checks if this node is modifiable.

        Raises:
            DOMException:
            - `NO_MODIFICATION_ALLOWED_ERR`: Raised when the node is readonly.
        """
        if self._read_only:
            raise DOMException(DOMException.NO_MODIFICATION_ALLOWED_ERR)

    @property
    def node_name(self) -> DOMString:
        """Read only; The name of this node, depending on its type.
        """
        return self._node_name

    def _set_node_name(self, name: DOMString) -> None:
        """Indirect accessor to set the 'node_name' property.
        """
        self._node_name = DOMString(name)

    @property
    def node_value(self) -> DOMString:
        """The value of this node, depending on its type.

        Raises:
            DOMException:
            - `NO_MODIFICATION_ALLOWED_ERR`: Raised when the node is readonly. (on setting)
            - `DOMSTRING_SIZE_ERR`: Raised when it would return more characters than fit in a `DOMString` variable on the implementation platform. (on retrieval)
        """
        return self._node_value

    @node_value.setter
    def node_value(self, value: DOMString) -> None:
        self._set_node_value(value)

    def _set_node_value(self, value: DOMString) -> None:
        """Indirect accessor to set the 'node_value' property.

        Raises:
            DOMException:
            - `NO_MODIFICATION_ALLOWED_ERR`: Raised when the node is readonly.
        """
        self._check_modifiable()
        self._node_value = DOMString(value)

    @property
    def node_type(self) -> NodeType:
        """Read only; A code representing the type of the underlying object, as defined in `NodeType`.
        """
        return self._node_type

    def _set_node_type(self, node_type: NodeType) -> None:
        """Indirect accessor to set the 'node_type' property.
        """
        if node_type not in NodeType:
            raise ValueError(f'{node_type} is not a valid code '
                             'for a node type.')
        self._node_type = node_type

    @property
    def parent_node(self) -> Optional[_AnyNode]:
        """The parent of this node. All nodes, except `Document`, `DocumentFragment`, and `Attr` may have a parent. However, if a node has just been created and not yet added to the tree, or if it has been removed from the tree, this is `None`.
        """
        return self._parent_node

    def _set_parent_node(self,
                         parent_node: Optional[_AnyNode]) -> None:
        """Indirect accessor to set the 'node_type' property.
        """
        if not parent_node:
            self._parent_node = None
        else:
            self._parent_node = parent_node

    @property
    def child_nodes(self) -> NodeList:
        """A `NodeList` that contains all children of this node. If there are no children, this is a `NodeList` containing no nodes. The content of the returned `NodeList` is "live" in the sense that, for instance, changes to the children of the node object that it was created from are immediately reflected in the nodes returned by the `NodeList` accessors; it is not a static snapshot of the content of the node. This is true for every `NodeList`, including the ones returned by the `getElementsByTagName` method.
        """
        return self._child_nodes

    def _init_child_nodes(self,
                          child_nodes: Optional[Iterable[_AnyNode]] = None) -> None:
        """Accessor to set the 'child_nodes' property.
        """
        if child_nodes is None:
            self._child_nodes = NodeList()
        else:
            self._child_nodes = NodeList(iter(child_nodes))

    @property
    def first_child(self) -> Optional[_AnyNode]:
        """The first child of this node. If there is no such node, this returns `None`.
        """
        if not self.child_nodes:
            return None
        return self.child_nodes.item(0)

    @property
    def last_child(self) -> Optional[_AnyNode]:
        """The last child of this node. If there is no such node, this returns `None`.
        """
        if not self.child_nodes:
            return None
        return self.child_nodes.item(self.child_nodes.length-1)

    @property
    def previous_sibling(self) -> Optional[_AnyNode]:
        """The node immediately preceding this node. If there is no such node, this returns `None`.
        """
        if self.parent_node is None:
            return None
        if self.parent_node.first_child is self:
            return None
        nth_child = self._nth_child_of_parent()
        return self.parent_node.child_nodes.item(nth_child-1)

    @property
    def next_sibling(self) -> Optional[_AnyNode]:
        """The node immediately following this node. If there is no such node, this returns `None`.
        """
        if self.parent_node is None:
            return None
        if self.parent_node.last_child is self:
            return None
        nth_child = self._nth_child_of_parent()
        return self.parent_node.child_nodes.item(nth_child+1)

    def _nth_child_of_parent(self) -> Optional[int]:
        """Accessor that indicates how many siblings are there preceding this node. if there is no such parent node, this returns `None`.
        """
        if self.parent_node is None:
            return None
        return self.parent_node.child_nodes.index(self)

    @property
    def attributes(self) -> _NamedNodeMap:
        """A `NamedNodeMap` containing the attributes of this node (if it is an `Element`) or `None` otherwise.
        """
        return self._attributes

    def _init_attributes(self,
                         attributes: Optional[Iterable[_AnyNode]] = None) -> None:
        self._attributes: _NamedNodeMap = {}  # TODO: Replace with real NamedNodeMap #19
        if attributes is None:
            return
        for attr in iter(attributes):
            self._attributes.set_named_item(attr)

    @property
    def owner_document(self) -> Optional[_Document]:
        """The `Document` object associated with this node. This is also the `Document` object used to create new nodes. When this node is a `Document` this is `None`.
        """
        if self.node_type == NodeType.DOCUMENT_NODE:
            return None
        return self._owner_document

    def _set_owner_document(self,
                            owner_document: Optional[_Document] = None) -> None:
        """Indirect accessor to set the 'owner_document' property.
        """
        self._owner_document = owner_document


_AnyNode = Node
_NamedNodeMap = Dict[str, _AnyNode]  # TODO: Implement NamedNodeMap (#19)
_Document = Node  # TODO: Implement Document (#20)
