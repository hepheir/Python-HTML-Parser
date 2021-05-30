import enum


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