from __future__ import absolute_import
from __future__ import annotations

from typing import Optional

from python.dom.node.Node import Node
from python.dom.node.NodeType import NodeType

from python.dom.type_checking import AnyNode, Document


class Element(Node):
    """Interface Element

    By far the vast majority of objects (apart from text) that authors encounter when traversing a document are `Element` nodes. Assume the following XML document:


    ```html
    <elementExample id="demo">
      <subelement1/>
      <subelement2><subsubelement/></subelement2>
    </elementExample>
    ```

    When represented using DOM, the top node is an `Element` node for "elementExample", which contains two child `Element` nodes, one for "subelement1" and one for "subelement2". "subelement1" contains no child nodes.

    Elements may have attributes associated with them; since the `Element` interface inherits from `Node`, the generic `Node` interface method `getAttributes` may be used to retrieve the set of all attributes for an element. There are methods on the `Element` interface to retrieve either an `Attr` object by name or an attribute value by name. In XML, where an attribute value may contain entity references, an `Attr` object should be retrieved to examine the possibly fairly complex sub-tree representing the attribute value. On the other hand, in HTML, where all attributes have simple string values, methods to directly access an attribute value can safely be used as a convenience.
    """

    def __init__(self,
                 owner_document: Document,
                 parent_node: Optional[AnyNode],
                 read_only: bool) -> None:
        super().__init__(owner_document=owner_document,
                         node_type=NodeType.ELEMENT_NODE,
                         parent_node=parent_node,
                         read_only=read_only)
