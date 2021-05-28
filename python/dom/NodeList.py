from __future__ import absolute_import

from typing import Optional, Iterator

from python.dom.type_checking import AnyNode


class NodeList(list):
    """Interface NodeList

    The `NodeList` interface provides the abstraction of an ordered collection of nodes, without defining or constraining how this collection is implemented.

    The items in the `NodeList` are accessible via an integral index, starting from 0.
    """

    def __iter__(self) -> Iterator[AnyNode]:
        return super().__iter__()

    @property
    def length(self) -> int:
        """The number of nodes in the list. The range of valid child node indices is 0 to `length`-1 inclusive.
        """
        return len(self)

    def item(self, index: int) -> Optional[AnyNode]:
        """Returns the indexth item in the collection. If index is greater than or equal to the number of nodes in the list, this returns `None`.

        Args:
            index: Index into the collection.

        Returns:
            The node at the `index`th position in the NodeList, or `None` if that is not a valid index.
        """
        if 0 <= index < self.length:
            return self[index]
        else:
            return None
