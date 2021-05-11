#!/usr/bin/env python3

import unittest
from google_c2s15 import rearrange_name

class TestRearrage(unittest.TestCase):
    def test_basic(self):
        testcase = "Satyam, Dubey"
        expected = "Dubey Satyam"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Madam, Queen K."
        expected = "Queen K. Madam"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "Rogers"
        expected = "Rogers"
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()
