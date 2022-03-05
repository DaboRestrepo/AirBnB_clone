#!/usr/bin/python3
"""
Unittest for user([..])
"""
import pep8
import unittest
from models.user import User


class TestState(unittest.TestCase):
    """ Write unittests for the class State. """

    def test_pep8_conformance(self):
        """ Test that we conform to PEP8. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == '__main__':
    unittest.main()
