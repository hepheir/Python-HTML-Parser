from __future__ import annotations

from ctypes import c_ushort, c_ulong
from typing import Callable

from w3.python.core.type import DOMString


class DOMImplementation:
    """Interface DOMImplementation

    The `DOMImplementation` interface provides a number of methods for performing operations that are independent of any particular instance of the document object model.
    The DOM Level 1 does not specify a way of creating a document instance, and hence document creation is an operation specific to an implementation. Future Levels of the DOM specification are expected to provide methods for creating documents directly.
    """

    # TODO
    def has_feature(self,
                    feature: DOMString,
                    version: DOMString) -> bool:
        """<NOT IMPLEMENTED>
        Test if the DOM implementation implements a specific feature.

        Args:
            feature: The package name of the feature to test. In Level 1, the legal values are "HTML" and "XML" (case-insensitive).
            version: This is the version number of the package name to test. In Level 1, this is the string "1.0". If the version is not specified, supporting any version of the feature will cause the method to return true.

        Returns:
            `True` if the feature is implemented in the specified version, `False` otherwise.

        This method raises no exceptions.
        """
        raise NotImplementedError


class NodeList:
    item: Callable[[c_ulong], Node]
    length: c_ulong


class NamedNodeMap:
    getNamedItem: Callable[[DOMString], Node]
    setNamedItem: Callable[[Node], Node]
    removeNamedItem: Callable[[DOMString], Node]
    item: Callable[[c_ulong], Node]
    length: c_ulong


class Node:
    """Interface `Node`

    The `Node` interface is the primary datatype for the entire Document Object Model.
    It represents a single node in the document tree.
    While all objects implementing the `Node` interface expose methods for dealing with children, not all objects implementing the `Node` interface may have children.
    For example, `Text` nodes may not have children, and adding children to such nodes results in a `DOMException` being raised.

    The attributes `node_name`, `node_value` and attributes are included as a mechanism to get at node information without casting down to the specific derived interface.
    In cases where there is no obvious mapping of these attributes for a specific `node_type` (e.g., `node_value` for an Element or `attributes` for a Comment), this returns `None`.
    Note that the specialized interfaces may contain additional and more convenient mechanisms to get and set the relevant information.
    """

    # Definition group `NodeType`
    # An integer indicating which type of node this is.
    ELEMENT_NODE: c_ushort = c_ushort(1)
    ATTRIBUTE_NODE: c_ushort = c_ushort(2)
    TEXT_NODE: c_ushort = c_ushort(3)
    CDATA_SECTION_NODE: c_ushort = c_ushort(4)
    ENTITY_REFERENCE_NODE: c_ushort = c_ushort(5)
    ENTITY_NODE: c_ushort = c_ushort(6)
    PROCESSING_INSTRUCTION_NODE: c_ushort = c_ushort(7)
    COMMENT_NODE: c_ushort = c_ushort(8)
    DOCUMENT_NODE: c_ushort = c_ushort(9)
    DOCUMENT_TYPE_NODE: c_ushort = c_ushort(10)
    DOCUMENT_FRAGMENT_NODE: c_ushort = c_ushort(11)
    NOTATION_NODE: c_ushort = c_ushort(12)

    nodeName: DOMString
    nodeValue: DOMString
    nodeType: c_ushort
    parentNode: Node
    childNodes: NodeList
    firstChild: Node
    lastChild: Node
    previousSibling: Node
    nextSibling: Node
    attributes: NamedNodeMap
    ownerDocument: Document
    insertBefore: Callable[[Node, Node], Node]
    replaceChild: Callable[[Node, Node], Node]
    removeChild: Callable[[Node], Node]
    appendChild: Callable[[Node], Node]
    hasChildNodes: Callable[[], bool]
    cloneNodes: Callable[[bool], Node]


class DocumentFragment(Node):
    """Interface `DocumentFragment`

    `DocumentFragment` is a "lightweight" or "minimal" `Document` object.
    It is very common to want to be able to extract a portion of a document's tree or to create a new fragment of a document.
    Imagine implementing a user command like cut or rearranging a document by moving fragments around.
    It is desirable to have an object which can hold such fragments and it is quite natural to use a `Node` for this purpose.
    While it is true that a `Document` object could fulfil this role, a `Document` object can potentially be a heavyweight object, depending on the underlying implementation.
    What is really needed for this is a very lightweight object.
    `DocumentFragment` is such an object.

    Furthermore, various operations -- such as inserting nodes as children of another `Node` -- may take `DocumentFragment` objects as arguments; this results in all the child nodes of the `DocumentFragment` being moved to the child list of this node.

    The children of a `DocumentFragment` node are zero or more nodes representing the tops of any sub-trees defining the structure of the document.
    `DocumentFragment` nodes do not need to be well-formed XML documents (although they do need to follow the rules imposed upon well-formed XML parsed entities, which can have multiple top nodes).
    For example, a `DocumentFragment` might have only one child and that child node could be a `Text` node.
    Such a structure model represents neither an HTML document nor a well-formed XML document.

    When a `DocumentFragment` is inserted into a `Document` (or indeed any other `Node` that may take children) the children of the `DocumentFragment` and not the `DocumentFragment` itself are inserted into the `Node`.
    This makes the `DocumentFragment` very useful when the user wishes to create nodes that are siblings; the `DocumentFragment` acts as the parent of these nodes so that the user can use the standard methods from the `Node` interface, such as `insertBefore()` and `appendChild()`.
    """

    def __init__(self,
                 owner_document: Document,
                 read_only: bool = False) -> None:
        super().__init__(owner_document=owner_document,
                         node_type=Node.DOCUMENT_FRAGMENT_NODE,
                         node_name='#document-fragment',
                         node_value=None,
                         read_only=read_only)


class Attr(Node):
    name: DOMString
    specified: bool
    value: DOMString


class Element(Node):
    tagName: DOMString
    getAttribute: Callable[[DOMString], DOMString]
    setAttribute: Callable[[DOMString, DOMString], None]
    removeAttribute: Callable[[DOMString], None]
    getAttributeNode: Callable[[DOMString], Attr]
    setAttributeNode: Callable[[Attr], Attr]
    removeAttributeNode: Callable[[Attr], Attr]
    getElementsByTagName: Callable[[DOMString], NodeList]
    normalize: Callable[[], None]


class CharacterData(Node):
    data: DOMString
    length: c_ulong
    substringData: Callable[[c_ulong, c_ulong], DOMString]
    appendData: Callable[[DOMString], None]
    insertData: Callable[[c_ulong, DOMString], None]
    deleteData: Callable[[c_ulong, c_ulong], None]
    replaceData: Callable[[c_ulong, c_ulong, DOMString], None]


class Comment(CharacterData):
    pass


class Text(CharacterData):
    splitText: Callable[[c_ulong], Text]


class CDATASection(Text):
    pass


class DocumentType(Node):
    name: DOMString
    entities: NamedNodeMap
    notations: NamedNodeMap


class Notation(Node):
    publicId: DOMString
    systemId: DOMString


class Entity(Node):
    publicId: DOMString
    systemId: DOMString
    notationName: DOMString


class EntityReference(Node):
    pass


class ProcessingInstruction(Node):
    target: DOMString
    data: DOMString


class Document(Node):
    """Interface Document

    The `Document` interface represents the entire HTML or XML document.
    Conceptually, it is the root of the document tree, and provides the primary access to the document's data.

    Since elements, text nodes, comments, processing instructions, etc. cannot exist outside the context of a `Document`, the `Document` interface also contains the factory methods needed to create these objects.
    The `Node` objects created have a `ownerDocument`` attribute which associates them with the `Document` within whose context they were created.
    """

    doctype: DocumentType
    implementation: DOMImplementation
    documentElement: Element
    createElement: Callable[[Document, DOMString], Element]
    createDocumentFragment: Callable[[Document], DocumentFragment]
    createTextNode: Callable[[Document, DOMString], Text]
    createComment: Callable[[Document, DOMString], Comment]
    createCDATASection: Callable[[Document, DOMString], CDATASection]
    createProcessingInstruction: Callable[[
        Document, DOMString, DOMString], ProcessingInstruction]
    createAttribute: Callable[[Document, DOMString], Attr]
    createEntityReference: Callable[[Document, DOMString], EntityReference]
    getElementsByTagName: Callable[[Document, DOMString], NodeList]

    def __init__(self, read_only: bool = False) -> None:
        super().__init__(owner_document=None,
                         node_type=Node.DOCUMENT_NODE,
                         node_name='#document',
                         node_value=None,
                         read_only=read_only)
