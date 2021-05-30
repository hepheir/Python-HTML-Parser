from __future__ import absolute_import

from typing import Optional

from python.dom.core.interface.fundamental.Node import Node
from python.dom.core.interface.fundamental.Node import NodeType
from python.dom.core.type import AnyNode, Document


class DocumentFragment(Node):
    """Interface DocumentFragment

    `DocumentFragment` is a "lightweight" or "minimal" `Document` object. It is very common to want to be able to extract a portion of a document's tree or to create a new fragment of a document. Imagine implementing a user command like cut or rearranging a document by moving fragments around. It is desirable to have an object which can hold such fragments and it is quite natural to use a Node for this purpose. While it is true that a `Document` object could fulfil this role, a `Document` object can potentially be a heavyweight object, depending on the underlying implementation. What is really needed for this is a very lightweight object. `DocumentFragment` is such an object.

    Furthermore, various operations -- such as inserting nodes as children of another `Node` -- may take `DocumentFragment` objects as arguments; this results in all the child nodes of the `DocumentFragment` being moved to the child list of this node.

    The children of a `DocumentFragment` node are zero or more nodes representing the tops of any sub-trees defining the structure of the document. `DocumentFragment` nodes do not need to be well-formed XML documents (although they do need to follow the rules imposed upon well-formed XML parsed entities, which can have multiple top nodes). For example, a `DocumentFragment` might have only one child and that child node could be a `Text` node. Such a structure model represents neither an HTML document nor a well-formed XML document.

    When a `DocumentFragment` is inserted into a `Document` (or indeed any other `Node` that may take children) the children of the `DocumentFragment` and not the `DocumentFragment` itself are inserted into the `Node`. This makes the `DocumentFragment` very useful when the user wishes to create nodes that are siblings; the `DocumentFragment` acts as the parent of these nodes so that the user can use the standard methods from the Node interface, such as `insert_before()` and `append_child()`.
    """

    def __init__(self,
                 owner_document: Document,
                 parent_node: Optional[AnyNode] = None,
                 read_only: bool = False) -> None:
        super().__init__(owner_document=owner_document,
                         node_type=NodeType.DOCUMENT_FRAGMENT_NODE,
                         parent_node=parent_node,
                         read_only=read_only)
