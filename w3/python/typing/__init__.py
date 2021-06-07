"""Module for typing purpose only.
Do not import below classes for actual usage.
"""

from __future__ import annotations

from typing import Iterable, Optional, Union


_DOMString = str


class _ExceptionCode(int):
    INDEX_SIZE_ERR = 1
    DOMSTRING_SIZE_ERR = 2
    HIERARCHY_REQUEST_ERR = 3
    WRONG_DOCUMENT_ERR = 4
    INVALID_CHARACTER_ERR = 5
    NO_DATA_ALLOWED_ERR = 6
    NO_MODIFICATION_ALLOWED_ERR = 7
    NOT_FOUND_ERR = 8
    NOT_SUPPORTED_ERR = 9
    INUSE_ATTRIBUTE_ERR = 10


class _DOMException(Exception):
    code: int


class _DOMImplementation:
    def hasFeature(self,
                   feature: _DOMString,
                   version: _DOMString) -> bool: pass


class _NodeType(int):
    ELEMENT_NODE = 1
    ATTRIBUTE_NODE = 2
    TEXT_NODE = 3
    CDATA_SECTION_NODE = 4
    ENTITY_REFERENCE_NODE = 5
    ENTITY_NODE = 6
    PROCESSING_INSTRUCTION_NODE = 7
    COMMENT_NODE = 8
    DOCUMENT_NODE = 9
    DOCUMENT_TYPE_NODE = 10
    DOCUMENT_FRAGMENT_NODE = 11
    NOTATION_NODE = 12


class _Node:
    def __init__(self: _Node,
                 node_type: _NodeType,
                 node_name: _DOMString,
                 owner_document: Optional[_Document],
                 node_value: Optional[_DOMString] = None,
                 child_nodes: Optional[Iterable[_AnyNode]] = None,
                 attributes: Optional[Iterable[_AnyNode]] = None,
                 read_only: bool = False) -> None: pass
    node_value: _DOMString
    @property
    def node_name(self) -> _DOMString: pass
    @property
    def node_type(self) -> _NodeType: pass
    @property
    def parent_node(self) -> Optional[_AnyNode]: pass
    @property
    def child_nodes(self) -> _NodeList: pass
    @property
    def first_child(self) -> Optional[_AnyNode]: pass
    @property
    def last_child(self) -> Optional[_AnyNode]: pass
    @property
    def previous_sibling(self) -> Optional[_AnyNode]: pass
    @property
    def next_sibling(self) -> Optional[_AnyNode]: pass
    @property
    def attributes(self) -> _NamedNodeMap: pass
    @property
    def owner_document(self) -> Optional[_Document]: pass

    def insert_before(self,
                      new_child: _AnyNode,
                      ref_child: Optional[_AnyNode] = None) -> _AnyNode: pass

    def replace_child(self,
                      new_child: _AnyNode,
                      old_child: _AnyNode) -> _AnyNode: pass
    def remove_child(self,
                     old_child: _AnyNode) -> _AnyNode: pass

    def append_child(self, new_child: _AnyNode) -> _AnyNode: pass
    def has_child_nodes(self) -> bool: pass
    def clone_node(self, deep: bool = False) -> _AnyNode: pass


class _NodeList:
    @property
    def length(self) -> int: pass
    def item(self, index: int) -> _Node: pass


class _NamedNodeMap:
    def getNamedItem(self, name: _DOMString) -> _Node: pass
    def setNamedItem(self, arg: _Node) -> _Node: pass
    def removeNamedItem(self, name: _DOMString) -> _Node: pass
    def item(self, index: int) -> _Node: pass
    @property
    def length(self) -> int: pass


class _DocumentFragment(_Node):
    pass


class _Document(_Node):
    @property
    def doctype(self) -> _DocumentType: pass
    @property
    def implementation(self) -> _DOMImplementation: pass
    @property
    def documentElement(self) -> _Element: pass
    def createElement(self, tagName: _DOMString) -> _Element: pass
    def createDocumentFragment(self) -> _DocumentFragment: pass
    def createTextNode(self, data: _DOMString) -> _Text: pass
    def createComment(self, data: _DOMString) -> _Comment: pass
    def createCDATASection(self, data: _DOMString) -> _CDATASection: pass

    def createProcessingInstruction(self,
                                    target: _DOMString,
                                    data: _DOMString) -> _ProcessingInstruction: pass

    def createAttribute(self, name: _DOMString) -> _Attr: pass
    def createEntityReference(self, name: _DOMString) -> _EntityReference: pass
    def getElementsByTagName(self, tagname: _DOMString) -> _NodeList: pass


class _CharacterData(_Node):
    data: _DOMString
    @property
    def length(self) -> int: pass

    def substringData(self,
                      offset: int,
                      count: int) -> _DOMString: pass

    def appendData(self,
                   arg: _DOMString) -> None: pass

    def insertData(self,
                   offset: int,
                   arg: _DOMString) -> None: pass

    def deleteData(self,
                   offset: int,
                   count: int) -> None: pass

    def replaceData(self,
                    offset: int,
                    count: int,
                    arg: _DOMString) -> None: pass


class _Attr(_Node):
    value: _DOMString
    @property
    def name(self) -> _DOMString: pass
    @property
    def specified(self) -> bool: pass


class _Element(_Node):
    @property
    def tagName(self) -> _DOMString: pass
    def getAttribute(self, name: _DOMString) -> _DOMString: pass

    def setAttribute(self,
                     name: _DOMString,
                     value: _DOMString) -> None: pass

    def removeAttribute(self, name: _DOMString) -> None: pass
    def getAttributeNode(self, name: _DOMString) -> _Attr: pass
    def setAttributeNode(self, newAttr: _Attr) -> _Attr: pass
    def removeAttributeNode(self, oldAttr: _Attr) -> _Attr: pass
    def getElementsByTagName(self, name: _DOMString) -> _NodeList: pass
    def normalize(self) -> None: pass


class _Text(_CharacterData):
    def splitText(self, offset: int) -> _Text: pass


class _Comment(_CharacterData):
    pass


class _CDATASection(_Text):
    pass


class _DocumentType(_Node):
    @property
    def name(self) -> _DOMString: pass
    @property
    def entities(self) -> _NamedNodeMap: pass
    @property
    def notations(self) -> _NamedNodeMap: pass


class _Notation(_Node):
    @property
    def publicId(self) -> _DOMString: pass
    @property
    def systemId(self) -> _DOMString: pass


class _Entity(_Node):
    @property
    def publicId(self) -> _DOMString: pass
    @property
    def systemId(self) -> _DOMString: pass
    @property
    def notationName(self) -> _DOMString: pass


class _EntityReference(_Node):
    pass


class _ProcessingInstruction(_Node):
    data: _DOMString
    @property
    def target(self) -> _DOMString: pass


_AnyNode = Union[_Node,
                 _Document,
                 _DocumentFragment,
                 _DocumentType,
                 _EntityReference,
                 _Element,
                 _Attr,
                 _ProcessingInstruction,
                 _Comment,
                 _Text,
                 _CDATASection,
                 _Entity,
                 _Notation]
