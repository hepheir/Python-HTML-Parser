class NodeList(list):
    """Interface NodeList

    The `NodeList` interface provides the abstraction of an ordered collection of nodes, without defining or constraining how this collection is implemented.

    The items in the `NodeList` are accessible via an integral index, starting from 0.
    """

    @property
    def length(self) -> int:
        """The number of nodes in the list. The range of valid child node indices is 0 to `length`-1 inclusive.
        """
        return len(self)
