import enum


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