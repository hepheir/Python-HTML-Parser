class DOMString(str):
    """The `DOMString` type

    To ensure interoperability, the DOM specifies the `DOMString` type as follows:

      * A `DOMString` is a sequence of 16-bit quantities. This may be expressed in IDL terms as:

            `typedef sequence<unsigned short> DOMString;`

      * Applications must encode `DOMString` using UTF-16 (defined in Appendix C.3 of [UNICODE] and Amendment 1 of [ISO-10646]).The UTF-16 encoding was chosen because of its widespread industry practice. Please note that for both HTML and XML, the document character set (and therefore the notation of numeric character references) is based on UCS-4. A single numeric character reference in a source document may therefore in some cases correspond to two array positions in a `DOMString` (a high surrogate and a low surrogate). Note: Even though the DOM defines the name of the string type to be `DOMString`, bindings may used different names. For, example for Java, `DOMString` is bound to the String type because it also uses UTF-16 as its encoding.

    > Note: As of August 1998, the OMG IDL specification included a wstring type. However, that definition did not meet the interoperability criteria of the DOM API since it relied on encoding negotiation to decide the width of a character.
    """
    pass
