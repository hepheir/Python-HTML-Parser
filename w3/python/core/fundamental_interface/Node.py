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
                 owner_document: Optional[_Document],
                 node_value: Optional[DOMString] = None,
                 child_nodes: Optional[Iterable[_AnyNode]] = None,
                 attributes: Optional[Iterable[_AnyNode]] = None,
                 read_only: bool = False) -> None:
        if node_value is None:
            node_value = ''
        self._read_only = False  # Allow to modify only while initiating.
        self._set_node_type(node_type)
        self._set_node_name(node_name)
        self._set_node_value(node_value)
        self._set_parent_node(None)
        self._init_child_nodes(child_nodes)
        self._init_attributes(attributes)
        self._set_owner_document(owner_document)
        self._read_only = bool(read_only)
        # Attributes
        self._node_type: NodeType
        self._node_name: DOMString
        self._node_value: DOMString
        self._parent_node: Optional[_AnyNode]
        self._child_nodes: NodeList
        self._attributes: _NamedNodeMap
        self._owner_document: Optional[_Document]
        self._read_only: bool

    @property
    def node_name(self) -> DOMString:
        """Read only; The name of this node, depending on its type."""
        return self._node_name

    def _set_node_name(self, name: DOMString) -> None:
        """Indirect accessor to set the 'node_name' property."""
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
        if self._read_only:
            raise DOMException(DOMException.NO_MODIFICATION_ALLOWED_ERR)
        self._node_value = DOMString(value)

    @property
    def node_type(self) -> NodeType:
        """Read only; A code representing the type of the underlying object, as defined in `NodeType`."""
        return self._node_type

    def _set_node_type(self, node_type: NodeType) -> None:
        """Indirect accessor to set the 'node_type' property."""
        if node_type not in NodeType:
            raise ValueError(f'{node_type} is not a valid code '
                             'for a node type.')
        self._node_type = node_type

    @property
    def parent_node(self) -> Optional[_AnyNode]:
        """The parent of this node.

        All nodes, except `Document`, `DocumentFragment`, and `Attr` may have a parent.
        However, if a node has just been created and not yet added to the tree, or if it has been removed from the tree, this is `None`.
        """
        return self._parent_node

    def _set_parent_node(self,
                         parent_node: Optional[_AnyNode]) -> None:
        """Indirect accessor to set the 'node_type' property."""
        if not parent_node:
            self._parent_node = None
        else:
            self._parent_node = parent_node

    @property
    def child_nodes(self) -> NodeList:
        """A `NodeList` that contains all children of this node.

        If there are no children, this is a `NodeList` containing no nodes.
        The content of the returned `NodeList` is "live" in the sense that, for instance, changes to the children of the node object that it was created from are immediately reflected in the nodes returned by the `NodeList` accessors; it is not a static snapshot of the content of the node.
        This is true for every `NodeList`, including the ones returned by the `getElementsByTagName` method.
        """
        return self._child_nodes

    def _init_child_nodes(self,
                          child_nodes: Optional[Iterable[_AnyNode]] = None) -> None:
        """Accessor to set the 'child_nodes' property."""
        if child_nodes is None:
            self._child_nodes = NodeList()
        else:
            self._child_nodes = NodeList(iter(child_nodes))

    @property
    def first_child(self) -> Optional[_AnyNode]:
        """The first child of this node.

        If there is no such node, this returns `None`.
        """
        if not self.has_child_nodes():
            return None
        return self.child_nodes.item(0)

    @property
    def last_child(self) -> Optional[_AnyNode]:
        """The last child of this node.

        If there is no such node, this returns `None`.
        """
        if not self.has_child_nodes():
            return None
        return self.child_nodes.item(self.child_nodes.length-1)

    @property
    def previous_sibling(self) -> Optional[_AnyNode]:
        """The node immediately preceding this node.

        If there is no such node, this returns `None`.
        """
        if self.parent_node is None:
            return None
        if self.parent_node.first_child is self:
            return None
        nth_child = self._nth_child_of_parent()
        return self.parent_node.child_nodes.item(nth_child-1)

    @property
    def next_sibling(self) -> Optional[_AnyNode]:
        """The node immediately following this node.

        If there is no such node, this returns `None`.
        """
        if self.parent_node is None:
            return None
        if self.parent_node.last_child is self:
            return None
        nth_child = self._nth_child_of_parent()
        return self.parent_node.child_nodes.item(nth_child+1)

    def _nth_child_of_parent(self) -> Optional[int]:
        """Accessor that indicates how many siblings are there preceding this node.

        If there is no such parent node, this returns `None`.
        """
        if self.parent_node is None:
            return None
        return self.parent_node.child_nodes.index(self)

    @property
    def attributes(self) -> _NamedNodeMap:
        """A `NamedNodeMap` containing the attributes of this node (if it is an `Element`) or `None` otherwise."""
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
        """The `Document` object associated with this node.

        This is also the `Document` object used to create new nodes.
        When this node is a `Document` this is `None`.
        """
        return self._owner_document

    def _set_owner_document(self,
                            owner_document: Optional[_Document] = None) -> None:
        """Indirect accessor to set the 'owner_document' property."""
        if owner_document is None:
            if self.node_type != NodeType.DOCUMENT_NODE:
                raise ValueError('`Node` should have a `Document` object ',
                                 'which associated with this node, ',
                                 'Unless this node is a `Document`.')
        self._owner_document = owner_document

    def insert_before(self,
                      new_child: _AnyNode,
                      ref_child: Optional[_AnyNode] = None) -> _AnyNode:
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
        if self._read_only:
            raise DOMException(DOMException.NO_MODIFICATION_ALLOWED_ERR)
        if self.owner_document is not new_child.owner_document:
            raise DOMException(DOMException.WRONG_DOCUMENT_ERR)
        # `HIERARCHY_REQUEST_ERR` should be checked on subclasses by overriding.
        if new_child in self.child_nodes:
            self.child_nodes.remove(new_child)
        if new_child.node_type == NodeType.DOCUMENT_FRAGMENT_NODE:
            grand_child_node: _AnyNode
            for grand_child_node in new_child.child_nodes:
                self.insert_before(grand_child_node, ref_child)
        elif ref_child is None:
            self.child_nodes.append(new_child)
        elif ref_child not in self.child_nodes:
            raise DOMException(DOMException.NOT_FOUND_ERR)
        else:
            self.child_nodes.insert(self.child_nodes.index(ref_child),
                                    new_child)
        new_child._set_parent_node(self)
        return new_child

    def append_child(self, new_child: _AnyNode) -> _AnyNode:
        """Adds the node `new_child` to the end of the list of children of this node.

        If the `new_child` is already in the tree, it is first removed.

        Args:
            new_child: The node to add. If it is a `DocumentFragment` object, the entire contents of the document fragment are moved into the child list of this node

        Returns:
            The node added.

        Raises:
            DOMException:
             -  `HIERARCHY_REQUEST_ERR`: Raised if this node is of a type that does not allow children of the type of the `new_child` node, or if the node to append is one of this node's ancestors.
             -  `WRONG_DOCUMENT_ERR`: Raised if `new_child` was created from a different document than the one that created this node.
             -  `NO_MODIFICATION_ALLOWED_ERR`: Raised if this node is readonly.
        """
        if self._read_only:
            raise DOMException(DOMException.NO_MODIFICATION_ALLOWED_ERR)
        if self.owner_document is not new_child.owner_document:
            raise DOMException(DOMException.WRONG_DOCUMENT_ERR)
        # `HIERARCHY_REQUEST_ERR` should be checked on subclasses by overriding.        # `HIERARCHY_REQUEST_ERR` should be checked on subclasses by overriding.
        if new_child in self.child_nodes:
            self.child_nodes.remove(new_child)
        if new_child.node_type == NodeType.DOCUMENT_FRAGMENT_NODE:
            grand_child_node: _AnyNode
            for grand_child_node in new_child.child_nodes:
                self.append_child(grand_child_node)
        else:
            new_child._set_parent_node(self)
            self.child_nodes.append(new_child)
        return new_child

    def has_child_nodes(self) -> bool:
        """This is a convenience method to allow easy determination of whether a node has any children.

        Returns:
            `True` if the node has any children, `False` if the node has no children.
        """
        return bool(self.child_nodes)


_AnyNode = Node
_NamedNodeMap = Dict[str, _AnyNode]  # TODO: Implement NamedNodeMap (#19)
_Document = Node  # TODO: Implement Document (#20)
