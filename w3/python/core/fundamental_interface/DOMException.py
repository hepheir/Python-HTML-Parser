import enum


class ExceptionCode(enum.IntEnum):
    """Definition group `ExceptionCode`
    An integer indicating the type of error generated.
    """
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


class DOMException(Exception):
    """Exception DOMException

    DOM operations only raise exceptions in "exceptional" circumstances, i.e., when an operation is impossible to perform (either for logical reasons, because data is lost, or because the implementation has become unstable). In general, DOM methods return specific error values in ordinary processing situation, such as out-of-bound errors when using `NodeList`.
    Implementations may raise other exceptions under other circumstances. For example, implementations may raise an implementation-dependent exception if a null argument is passed.
    Some languages and object systems do not support the concept of exceptions. For such systems, error conditions may be indicated using native error reporting mechanisms. For some bindings, for example, methods may return error codes similar to those listed in the corresponding method descriptions.
    """
    INDEX_SIZE_ERR = ExceptionCode.INDEX_SIZE_ERR
    DOMSTRING_SIZE_ERR = ExceptionCode.DOMSTRING_SIZE_ERR
    HIERARCHY_REQUEST_ERR = ExceptionCode.HIERARCHY_REQUEST_ERR
    WRONG_DOCUMENT_ERR = ExceptionCode.WRONG_DOCUMENT_ERR
    INVALID_CHARACTER_ERR = ExceptionCode.INVALID_CHARACTER_ERR
    NO_DATA_ALLOWED_ERR = ExceptionCode.NO_DATA_ALLOWED_ERR
    NO_MODIFICATION_ALLOWED_ERR = ExceptionCode.NO_MODIFICATION_ALLOWED_ERR
    NOT_FOUND_ERR = ExceptionCode.NOT_FOUND_ERR
    NOT_SUPPORTED_ERR = ExceptionCode.NOT_SUPPORTED_ERR
    INUSE_ATTRIBUTE_ERR = ExceptionCode.INUSE_ATTRIBUTE_ERR
