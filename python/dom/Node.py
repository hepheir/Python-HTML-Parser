class Node:
    """Interface `Node`

    The `Node` interface is the primary datatype for the entire Document Object Model. It represents a single node in the document tree. While all objects implementing the `Node` interface expose methods for dealing with children, not all objects implementing the `Node` interface may have children. For example, `Text` nodes may not have children, and adding children to such nodes results in a `DOMException` being raised.

    The attributes `nodeName`, `nodeValue` and attributes are included as a mechanism to get at node information without casting down to the specific derived interface. In cases where there is no obvious mapping of these attributes for a specific `nodeType` (e.g., `nodeValue` for an Element or `attributes` for a Comment), this returns `None`. Note that the specialized interfaces may contain additional and more convenient mechanisms to get and set the relevant information.
    """
    pass
