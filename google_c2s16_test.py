#!/usr/bin/env python3

import unittest

from google_c2s16 import validate_user

class TestValidateUser(unittest.TestCase):

    def test_valid(self):
        self.assertEqual(validate_user("Satyam", 3), True)

    def test_too_short(self):
        self.assertEqual(validate_user("Satyam", 1), True)

    def test_invalid_characters(self):
        self.assertEqual(validate_user("invalid_user", 1), False)

    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validate_user, "Sam", -1)

# Run the Test
unittest.main()
