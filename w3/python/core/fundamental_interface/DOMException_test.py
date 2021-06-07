import unittest

from w3.dom import DOMException


class TestProperty_Code(unittest.TestCase):
    def test_raise_INDEX_SIZE_ERR(self):
        with self.assertRaises(DOMException) as context_manager:
            raise DOMException(DOMException.INDEX_SIZE_ERR)
            self.fail()
        self.assertEqual(context_manager.exception.code,
                         DOMException.INDEX_SIZE_ERR)


if __name__ == '__main__':
    unittest.main()
