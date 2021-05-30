from __future__ import absolute_import
from __future__ import annotations

from typing import Optional

from python.dom.node.Node import Node
from python.dom.node.NodeType import NodeType

from python.dom.type_checking import AnyNode, Document


class Comment(Node):
    """Interface Comment

    This represents the content of a comment, i.e., all the characters between the starting '<!--' and ending '-->'. Note that this is the definition of a comment in XML, and, in practice, HTML, although some HTML tools may implement the full SGML comment structure.
    """

    def __init__(self,
                 owner_document: Document,
                 parent_node: Optional[AnyNode],
                 read_only: bool) -> None:
        super().__init__(owner_document=owner_document,
                         node_type=NodeType.COMMENT_NODE,
                         parent_node=parent_node,
                         read_only=read_only)
