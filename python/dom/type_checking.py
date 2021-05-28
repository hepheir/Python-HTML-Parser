from __future__ import absolute_import

from typing import Union, TYPE_CHECKING

AnyNode = None

if TYPE_CHECKING:
    from python.dom.NotImplemented import *
    from python.dom.DOMException import DOMException
    from python.dom.DOMString import DOMString
    from python.dom.Node import Node
    from python.dom.NodeList import NodeList

    AnyNode = Union[
        Node,
        # Ordered by NodeType
        Element,
        Attr,
        Text,
        CDATASection,
        EntityReference,
        Entity,
        ProcessingInstruction,
        Comment,
        Document,
        DocumentType,
        DocumentFragment,
        Notation,
    ]
