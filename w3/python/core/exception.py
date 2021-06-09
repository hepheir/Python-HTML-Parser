from ctypes import c_ushort


class DOMException(Exception):
    """Exception `DOMException`

    DOM operations only raise exceptions in "exceptional" circumstances, i.e., when an operation is impossible to perform
    (either for logical reasons, because data is lost, or because the implementation has become unstable).
    In general, DOM methods return specific error values in ordinary processing situation, such as out-of-bound errors when using `NodeList`.

    Implementations may raise other exceptions under other circumstances.
    For example, implementations may raise an implementation-dependent exception if a `None` argument is passed.

    Some languages and object systems do not support the concept of exceptions.
    For such systems, error conditions may be indicated using native error reporting mechanisms.
    For some bindings, for example, methods may return error codes similar to those listed in the corresponding method descriptions.
    """

    # Definition group `ExceptionCode`
    # An integer indicating the type of error generated.
    INDEX_SIZE_ERR: c_ushort = c_ushort(1)
    DOMSTRING_SIZE_ERR: c_ushort = c_ushort(2)
    HIERARCHY_REQUEST_ERR: c_ushort = c_ushort(3)
    WRONG_DOCUMENT_ERR: c_ushort = c_ushort(4)
    INVALID_CHARACTER_ERR: c_ushort = c_ushort(5)
    NO_DATA_ALLOWED_ERR: c_ushort = c_ushort(6)
    NO_MODIFICATION_ALLOWED_ERR: c_ushort = c_ushort(7)
    NOT_FOUND_ERR: c_ushort = c_ushort(8)
    NOT_SUPPORTED_ERR: c_ushort = c_ushort(9)
    INUSE_ATTRIBUTE_ERR: c_ushort = c_ushort(10)

    def __init__(self, error_code: c_ushort, *args: object) -> None:
        super().__init__(*args)
        self.code: c_ushort = error_code
