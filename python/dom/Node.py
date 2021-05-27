import enum
from typing import AnyStr

from python.dom.DOMString import DOMString


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

    The attributes `node_name`, `nodeValue` and attributes are included as a mechanism to get at node information without casting down to the specific derived interface. In cases where there is no obvious mapping of these attributes for a specific `node_type` (e.g., `nodeValue` for an Element or `attributes` for a Comment), this returns `None`. Note that the specialized interfaces may contain additional and more convenient mechanisms to get and set the relevant information.
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
                 read_only: bool = False) -> None:
        self._node_type: NodeType = node_type
        self._read_only: bool = read_only

    @property
    def node_name(self) -> DOMString:
        """The name of this node, depending on its type.
        """
        raise NotImplementedError

    @property
    def node_type(self) -> NodeType:
        """A code representing the type of the underlying object.
        """
        return self._node_type
