from __future__ import absolute_import
from __future__ import annotations

from typing import Optional

from python.dom.node.Node import Node
from python.dom.node.NodeType import NodeType

from python.dom.type_checking import AnyNode, Document


class Attr(Node):
    """Interface Attr

    The `Attr` interface represents an attribute in an `Element` object. Typically the allowable values for the attribute are defined in a document type definition.

    `Attr` objects inherit the `Node` interface, but since they are not actually child nodes of the element they describe, the DOM does not consider them part of the document tree. Thus, the `Node` attributes `parent_node`, `previous_sibling`, and `next_sibling` have a `None` value for `Attr` objects. The DOM takes the view that attributes are properties of elements rather than having a separate identity from the elements they are associated with; this should make it more efficient to implement such features as default attributes associated with all elements of a given type. Furthermore, `Attr` nodes may not be immediate children of a `DocumentFragment`. However, they can be associated with `Element` nodes contained within a `DocumentFragment`. In short, users and implementors of the DOM need to be aware that `Attr` nodes have some things in common with other objects inheriting the Node interface, but they also are quite distinct.

    The attribute's effective value is determined as follows: if this attribute has been explicitly assigned any value, that value is the attribute's effective value; otherwise, if there is a declaration for this attribute, and that declaration includes a default value, then that default value is the attribute's effective value; otherwise, the attribute does not exist on this element in the structure model until it has been explicitly added. Note that the nodeValue attribute on the `Attr` instance can also be used to retrieve the string version of the attribute's value(s).

    In XML, where the value of an attribute can contain entity references, the child nodes of the `Attr` node provide a representation in which entity references are not expanded. These child nodes may be either `Text` or `EntityReference` nodes. Because the attribute type may be unknown, there are no tokenized attribute values.
    """

    def __init__(self,
                 owner_document: Document,
                 parent_node: Optional[AnyNode],
                 read_only: bool) -> None:
        super().__init__(owner_document=owner_document,
                         node_type=NodeType.ATTRIBUTE_NODE,
                         parent_node=parent_node,
                         read_only=read_only)
