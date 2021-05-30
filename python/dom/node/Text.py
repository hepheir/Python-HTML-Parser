from __future__ import absolute_import
from __future__ import annotations

from typing import Optional

from python.dom.node.Node import Node
from python.dom.node.NodeType import NodeType

from python.dom.type_checking import AnyNode, Document


class Text(Node):
    """Interface Text

    The `Text` interface represents the textual content (termed character data in XML) of an `Element` or `Attr`. If there is no markup inside an element's content, the text is contained in a single object implementing the `Text` interface that is the only child of the element. If there is markup, it is parsed into a list of elements and `Text` nodes that form the list of children of the element.

    When a document is first made available via the DOM, there is only one `Text` node for each block of text. Users may create adjacent `Text` nodes that represent the contents of a given element without any intervening markup, but should be aware that there is no way to represent the separations between these nodes in XML or HTML, so they will not (in general) persist between DOM editing sessions. The `normalize()` method on `Element` merges any such adjacent `Text` objects into a single node for each block of text; this is recommended before employing operations that depend on a particular document structure, such as navigation with `XPointers`.
    """

    def __init__(self,
                 owner_document: Document,
                 parent_node: Optional[AnyNode],
                 read_only: bool) -> None:
        super().__init__(owner_document=owner_document,
                         node_type=NodeType.ELEMENT_NODE,
                         parent_node=parent_node,
                         read_only=read_only)
