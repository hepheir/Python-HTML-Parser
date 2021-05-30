from __future__ import absolute_import

from typing import Union, TYPE_CHECKING


if TYPE_CHECKING:
    from python.dom.core.interface.extended.CDATASection import CDATASection
    from python.dom.core.interface.extended.DocumentType import DocumentType
    from python.dom.core.interface.extended.Entity import Entity
    from python.dom.core.interface.extended.EntityReference import EntityReference
    from python.dom.core.interface.extended.Notation import Notation
    from python.dom.core.interface.extended.ProcessingInstruction import ProcessingInstruction
    from python.dom.core.interface.fundamental.Attr import Attr
    from python.dom.core.interface.fundamental.CharacterData import CharacterData
    from python.dom.core.interface.fundamental.Comment import Comment
    from python.dom.core.interface.fundamental.Document import Document
    from python.dom.core.interface.fundamental.DocumentFragment import DocumentFragment
    from python.dom.core.interface.fundamental.DOMException import DOMException
    from python.dom.core.interface.fundamental.DOMImplementation import DOMImplementation
    from python.dom.core.interface.fundamental.Element import Element
    from python.dom.core.interface.fundamental.NamedNodeMap import NamedNodeMap
    from python.dom.core.interface.fundamental.Node import Node
    from python.dom.core.interface.fundamental.Node import NodeType
    from python.dom.core.interface.fundamental.NodeList import NodeList
    from python.dom.core.interface.fundamental.Text import Text


    AnyNode = Union[
        # extended interfaces
        #   CDATASection,
        #   DocumentType,
        #   Entity,
        #   EntityReference,
        #   Notation,
        #   ProcessingInstruction,

        # fundamental interfaces
        Node,
        Element,
        Attr,
        Text,
        Comment,
        Document,
        DocumentFragment,
    ]
else:
    AnyNode = 'AnyNode'

    # Extended interfaces
    CDATASection = 'CDATASection'
    DocumentType = 'DocumentType'
    Entity = 'Entity'
    EntityReference = 'EntityReference'
    Notation = 'Notation'
    ProcessingInstruction = 'ProcessingInstruction'

    # Fundamental interfaces
    Attr = 'Attr'
    CharacterData = 'CharacterData'
    Comment = 'Comment'
    Document = 'Document'
    DocumentFragment = 'DocumentFragment'
    DOMException = 'DOMException'
    DOMImplementation = 'DOMImplementation'
    Element = 'Element'
    NamedNodeMap = 'NamedNodeMap'
    Node = 'Node'
    NodeType = 'NodeType'
    NodeList = 'NodeList'
    Text = 'Text'


class DOMString(str):
    """The `DOMString` type

    To ensure interoperability, the DOM specifies the `DOMString` type as follows:

      * A `DOMString` is a sequence of 16-bit quantities. This may be expressed in IDL terms as:

            `typedef sequence<unsigned short> DOMString;`

      * Applications must encode `DOMString` using UTF-16 (defined in Appendix C.3 of [UNICODE] and Amendment 1 of [ISO-10646]).The UTF-16 encoding was chosen because of its widespread industry practice. Please note that for both HTML and XML, the document character set (and therefore the notation of numeric character references) is based on UCS-4. A single numeric character reference in a source document may therefore in some cases correspond to two array positions in a `DOMString` (a high surrogate and a low surrogate). Note: Even though the DOM defines the name of the string type to be `DOMString`, bindings may used different names. For, example for Java, `DOMString` is bound to the String type because it also uses UTF-16 as its encoding.

    > Note: As of August 1998, the OMG IDL specification included a wstring type. However, that definition did not meet the interoperability criteria of the DOM API since it relied on encoding negotiation to decide the width of a character.
    """
    pass


del absolute_import
del Union
del TYPE_CHECKING
