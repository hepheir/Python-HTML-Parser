from __future__ import absolute_import

from typing import Union, TYPE_CHECKING

AnyNode = None

if TYPE_CHECKING:
    from python.dom.DOMException import DOMException
    from python.dom.DOMString import DOMString
    from python.dom.NodeList import NodeList
    from python.dom.node import Node
    from python.dom.node import Element
    from python.dom.node import Attr
    from python.dom.node import Text
    from python.dom.node import CDATASection
    from python.dom.node import EntityReference
    from python.dom.node import Entity
    from python.dom.node import ProcessingInstruction
    from python.dom.node import Comment
    from python.dom.node import Document
    from python.dom.node import DocumentType
    from python.dom.node import DocumentFragment
    from python.dom.node import Notation

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
