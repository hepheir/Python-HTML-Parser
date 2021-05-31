import unittest

from w3.python.core.fundamental_interface.DOMException import DOMException


class Test_DOMException(unittest.TestCase):
    def test_raise_INDEX_SIZE_ERR(self):
        try:
            raise DOMException(DOMException.INDEX_SIZE_ERR)
        except DOMException as e:
            code = e.args[0]
            self.assertEqual(code, DOMException.INDEX_SIZE_ERR)
        else:
            self.fail()


if __name__ == '__main__':
    unittest.main()
