from w3.python.typing import _DOMString


class DOMImplementation:
    """Interface DOMImplementation

    The `DOMImplementation` interface provides a number of methods for performing operations that are independent of any particular instance of the document object model.
    The DOM Level 1 does not specify a way of creating a document instance, and hence document creation is an operation specific to an implementation. Future Levels of the DOM specification are expected to provide methods for creating documents directly.
    """

    # TODO
    def has_feature(self,
                    feature: _DOMString,
                    version: _DOMString) -> bool:
        """<NOT IMPLEMENTED>
        Test if the DOM implementation implements a specific feature.

        Args:
            feature: The package name of the feature to test. In Level 1, the legal values are "HTML" and "XML" (case-insensitive).
            version: This is the version number of the package name to test. In Level 1, this is the string "1.0". If the version is not specified, supporting any version of the feature will cause the method to return true.

        Returns:
            `True` if the feature is implemented in the specified version, `False` otherwise.

        This method raises no exceptions.
        """
        raise NotImplementedError
