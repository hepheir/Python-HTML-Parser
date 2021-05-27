import enum
import warnings
from typing import AnyStr, Optional

from python.dom.DOMException import DOMException
from python.dom.DOMString import DOMString
from python.dom.NotImplemented.NodeList import NodeList
from python.dom.type_checking import AnyNode


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
    ATTRIBUTE_NODE = NodeType.ATTRIBUTE_NODE
    TEXT_NODE = NodeType.TEXT_NODE
    ELEMENT_NODE = NodeType.ELEMENT_NODE
    CDATA_SECTION_NODE = NodeType.CDATA_SECTION_NODE
    ENTITY_REFERENCE_NODE = NodeType.ENTITY_REFERENCE_NODE
    ENTITY_NODE = NodeType.ENTITY_NODE
    PROCESSING_INSTRUCTION_NODE = NodeType.PROCESSING_INSTRUCTION_NODE
    COMMENT_NODE = NodeType.COMMENT_NODE
    DOCUMENT_NODE = NodeType.DOCUMENT_NODE
    DOCUMENT_TYPE_NODE = NodeType.DOCUMENT_TYPE_NODE
    DOCUMENT_FRAGMENT_NODE = NodeType.DOCUMENT_FRAGMENT_NODE
    NOTATION_NODE = NodeType.NOTATION_NODE

    def __init__(self,
                 node_type: NodeType,
                 parent_node: Optional[AnyNode] = None,
                 read_only: bool = False) -> None:
        self._set_parent_node(parent_node, node_type)
        self._node_type: NodeType = node_type
        self._read_only: bool = read_only
        self._parent_node: Optional[AnyNode] # parent node should be set with `_set_parent_node` method.
        self._child_nodes: NodeList = NodeList()
        self._previous_sibling: Optional[AnyNode] = None
        self._next_sibling: Optional[AnyNode] = None


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
    def node_value(self, value: AnyStr) -> None:
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
            if self.node_type in [Node.DOCUMENT_NODE,
                                  Node.DOCUMENT_FRAGMENT_NODE,
                                  Node.ATTRIBUTE_NODE]:
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
        if self.child_nodes.length == 0:
            return None
        else:
            return self.child_nodes.item(0)

    @property
    def last_child(self) -> Optional[AnyNode]:
        """The last child of this node. If there is no such node, this returns `None`.
        """
        if self.child_nodes.length == 0:
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
