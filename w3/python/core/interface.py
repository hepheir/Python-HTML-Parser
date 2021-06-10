from __future__ import annotations

from ctypes import c_ushort, c_ulong
from typing import Callable, Optional

from w3.python.core.exception import DOMException
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

    def __init__(self) -> None:
        # Accessor about this node's modification
        self._read_only: bool
        # Accessors about this node's properties
        self._node_type: c_ushort
        self._node_name: DOMString
        self._node_value: DOMString
        self._attributes: NamedNodeMap
        # Accessors about DOM Tree
        self._owner_document: Optional[Document]
        self._parent_node: Optional[Node]
        self._next_sibling_node: Optional[Node]
        self._prev_sibling_node: Optional[Node]
        self._child_nodes: NodeList
        # Methods typing hints
        self.insertBefore: Callable[[Node, Node], Node]
        self.replaceChild: Callable[[Node, Node], Node]
        self.removeChild: Callable[[Node], Node]
        self.appendChild: Callable[[Node], Node]
        self.hasChildNodes: Callable[[], bool]
        self.cloneNodes: Callable[[bool], Node]

    def _get_nodeName(self) -> DOMString:
        """Indirect accessor to get the `nodeName` property."""
        return self._node_name

    def _set_nodeName(self, name: DOMString) -> None:
        """Indirect accessor to set the `nodeName` property."""
        self._node_name = DOMString(name)

    def _get_nodeValue(self) -> DOMString:
        """Indirect accessor to get the `nodeValue` property.

        Raises:
            DOMException:
            -   DOMSTRING_SIZE_ERR: Raised when it would return more characters than fit in a `DOMString` variable on the implementation platform.
        """
        # XXX: DOMException.DOMSTRING_SIZE_ERR was not taken into account.
        return self._node_value

    def _set_nodeValue(self, value: DOMString) -> None:
        """Indirect accessor to set the `nodeValue` property."""
        self._node_value = DOMString(value)

    def _get_nodeType(self) -> c_ushort:
        """Indirect accessor to get the `nodeType` property."""
        return self._node_type

    def _set_nodeType(self, type: c_ushort) -> None:
        """Indirect accessor to set the `nodeType` property."""
        self._node_type = c_ushort(type)

    def _get_parentNode(self) -> Node:
        """Indirect accessor to get the `parentNode` property."""
        return self._parent_node

    def _set_parentNode(self, node: Optional[Node] = None) -> None:
        """Indirect accessor to set the `parentNode` property."""
        self._parent_node = node

    def _get_childNodes(self) -> NodeList:
        """Indirect accessor to get the `childNodes` property."""
        return self._child_nodes

    def _get_firstChild(self) -> Optional[Node]:
        """Indirect accessor to get the `firstChild` property."""
        raise NotImplementedError()

    def _get_lastChild(self) -> Node:
        """Indirect accessor to get the `lastChild` property."""
        raise NotImplementedError()

    def _get_previousSibling(self) -> Node:
        """Indirect accessor to get the `previousSibling` property."""
        return self._prev_sibling_node

    def _get_nextSibling(self) -> Node:
        """Indirect accessor to get the `nextSibling` property."""
        return self._next_sibling_node

    def _get_attributes(self) -> NamedNodeMap:
        """Indirect accessor to get the `attributes` property."""
        return self._attributes

    def _get_ownerDocument(self) -> Document:
        """Indirect accessor to get the `ownerDocument` property."""
        return self._owner_document

    def _set_ownerDocument(self, owner_document: Document) -> None:
        """Indirect accessor to set the `ownerDocument` property."""
        self._owner_document = owner_document

    @property
    def nodeName(self) -> DOMString:
        """The name of this node, depending on its type."""
        return self._get_nodeName()

    @property
    def nodeValue(self) -> DOMString:
        """The value of this node, depending on its type.

        Raises:
            Exceptions on setting
                DOMException:
                    NO_MODIFICATION_ALLOWED_ERR: Raised when the node is readonly.

            Exceptions on retrieval
                DOMException:
                    DOMSTRING_SIZE_ERR: Raised when it would return more characters than fit in a `DOMString` variable on the implementation platform.
        """
        return self._get_nodeValue()

    @nodeValue.setter
    def nodeValue(self, value: DOMString) -> None:
        self._set_nodeValue(value)

    @property
    def nodeType(self) -> c_ushort:
        """A code representing the type of the underlying object."""
        return self._get_nodeType()

    @property
    def parentNode(self) -> Optional[Node]:
        """The parent of this node.

        All nodes, except `Document`, `DocumentFragment`, and `Attr` may have a parent.
        However, if a node has just been created and not yet added to the tree, or if it has been removed from the tree, this is `None`.
        """
        return self._get_parentNode()

    @property
    def childNodes(self) -> NodeList:
        """A `NodeList` that contains all children of this node.

        If there are no children, this is a `NodeList` containing no nodes.
        The content of the returned `NodeList` is "live" in the sense that, for instance, changes to the children of the node object that it was created from are immediately reflected in the nodes returned by the `NodeList` accessors; it is not a static snapshot of the content of the node.
        This is true for every `NodeList`, including the ones returned by the `getElementsByTagName` method.
        """
        return self._get_childNodes()

    @property
    def firstChild(self) -> Node:
        """The first child of this node.

        If there is no such node, this returns `null`."""
        return self._get_firstChild()

    @property
    def lastChild(self) -> Node:
        """The last child of this node.

        If there is no such node, this returns `null`."""
        return self._get_lastChild()

    @property
    def previousSibling(self) -> Node:
        """The node immediately preceding this node.

        If there is no such node, this returns `null`."""
        return self._get_previousSibling()

    @property
    def nextSibling(self) -> Node:
        """The node immediately following this node.

        If there is no such node, this returns `None`.
        """
        return self._get_nextSibling()

    @property
    def attributes(self) -> NamedNodeMap:
        """A `NamedNodeMap` containing the attributes of this node (if it is an `Element`) or `None` otherwise.
        """
        return self._get_attributes()

    @property
    def ownerDocument(self) -> Document:
        """The `Document` object associated with this node.

        This is also the `Document` object used to create new nodes.
        When this node is a `Document` this is `None`.
        """
        return self._get_ownerDocument()

    def insertBefore(self, newChild: Node, refChild: Node) -> Node:
        """Inserts the node `newChild` before the existing child node `refChild`.

        If `refChild` is `None`, insert `newChild` at the end of the list of children.
        If `newChild` is a `DocumentFragment` object, all of its children are inserted, in the same order, before `refChild`.
        If the `newChild` is already in the tree, it is first removed.

        Args:
            newChild: The node to insert.
            refChild: The reference node, i.e., the node before which the new node must be inserted.

        Returns:
            The node being inserted.

        Raises:
            DOMException:
            -   HIERARCHY_REQUEST_ERR: Raised if this node is of a type that does not allow children of the type of the `newChild` node, or if the node to insert is one of this node's ancestors.
            -   WRONG_DOCUMENT_ERR: Raised if `newChild` was created from a different document than the one that created this node.
            -   NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.
            -   NOT_FOUND_ERR: Raised if `refChild` is not a child of this node.
        """
        raise NotImplementedError()

    def replaceChild(self, newChild: Node, oldChild: Node) -> Node:
        """Replaces the child node `oldChild` with `newChild` in the list of children, and returns the `oldChild` node.

        If the `newChild` is already in the tree, it is first removed.

        Args:
            newChild: The new node to put in the child list.
            oldChild: The node being replaced in the list.

        Returns:
            The node replaced.

        Raises:
            DOMException:
            -   HIERARCHY_REQUEST_ERR: Raised if this node is of a type that does not allow children of the type of the `newChild` node, or it the node to put in is one of this node's ancestors.
            -   WRONG_DOCUMENT_ERR: Raised if `newChild` was created from a different document than the one that created this node.
            -   NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.
            -   NOT_FOUND_ERR: Raised if `oldChild` is not a child of this node.
        """
        raise NotImplementedError()

    def removeChild(self, oldChild: Node) -> Node:
        """Removes the child node indicated by `oldChild` from the list of children, and returns it.

        Args:
            oldChild: The node being removed.

        Returns:
            The node removed.

        Raises:
            DOMException:
            -   NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.
            -   NOT_FOUND_ERR: Raised if `oldChild` is not a child of this node.
        """
        raise NotImplementedError()

    def appendChild(self, newChild: Node) -> Node:
        """Adds the node `newChild` to the end of the list of children of this node.

        If the `newChild` is already in the tree, it is first removed.

        Args:
            newChild: The node to add. If it is a `DocumentFragment` object, the entire contents of the document fragment are moved into the child list of this node

        Returns:
            The node added.

        Raises:
            DOMException:
            -   HIERARCHY_REQUEST_ERR: Raised if this node is of a type that does not allow children of the type of the `newChild` node, or if the node to append is one of this node's ancestors.
            -   WRONG_DOCUMENT_ERR: Raised if `newChild` was created from a different document than the one that created this node.
            -   NO_MODIFICATION_ALLOWED_ERR: Raised if this node is readonly.
        """
        raise NotImplementedError()

    def hasChildNodes(self) -> bool:
        """This is a convenience method to allow easy determination of whether a node has any children.

        Returns:
            `True` if the node has any children, `False` if the node has no children.

        This method has no parameters.
        This method raises no exceptions.
        """
        raise NotImplementedError()

    def cloneNode(self) -> Node:
        """Returns a duplicate of this node, i.e., serves as a generic copy constructor for nodes.

        The duplicate node has no parent (`parentNode` returns `None`.).
        Cloning an `Element` copies all attributes and their values, including those generated by the XML processor to represent defaulted attributes, but this method does not copy any text it contains unless it is a deep clone, since the text is contained in a child `Text` node.
        Cloning any other type of node simply returns a copy of this node.

        Args:
            deep: If `True`, recursively clone the subtree under the specified node; if `False`, clone only the node itself (and its attributes, if it is an `Element`).

        Returns:
            The duplicate node.

        This method raises no exceptions.
        """
        raise NotImplementedError()


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
