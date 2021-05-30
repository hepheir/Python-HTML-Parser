from __future__ import absolute_import

from python.dom.core.interface.fundamental.Node import Node
from python.dom.core.interface.fundamental.Node import NodeType


class Document(Node):
    """Interface Document

    The `Document` interface represents the entire HTML or XML document. Conceptually, it is the root of the document tree, and provides the primary access to the document's data.

    Since elements, text nodes, comments, processing instructions, etc. cannot exist outside the context of a `Document`, the `Document` interface also contains the factory methods needed to create these objects. The Node objects created have a `owner_document` attribute which associates them with the `Document` within whose context they were created.
    """

    def __init__(self, read_only: bool = False) -> None:
        super().__init__(owner_document=self,
                         node_type=NodeType.DOCUMENT_NODE,
                         parent_node=None,
                         read_only=read_only)
