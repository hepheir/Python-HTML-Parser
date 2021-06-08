from w3.python.core.type import DOMString
from w3.python.core.fundamental_interface.Node import Node
from w3.python.core.fundamental_interface.Node import NodeType
from w3.python.typing import _Document


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
                 owner_document: _Document,
                 read_only: bool = False) -> None:
        super().__init__(owner_document=owner_document,
                         node_type=NodeType.DOCUMENT_FRAGMENT_NODE,
                         node_name='#document-fragment',
                         node_value=None,
                         read_only=read_only)
