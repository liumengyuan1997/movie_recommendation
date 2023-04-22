"""
Tests of utility functions that help with run.py

NAME: Mengyuan Liu
SEMESTER: Spring 2023
"""
import unittest
from utils import *


class TestFunctions(unittest.TestCase):

    def test_check_number(self):
        """ Test valid input """
        self.assertTrue(check_number('3.5'))
        self.assertTrue(check_number('-10.5'))
        self.assertTrue(check_number('0'))
        self.assertTrue(check_number('4'))

        """ Test invalid input """
        self.assertFalse(check_number('3.a'))
        self.assertFalse(check_number('3,5'))
        self.assertFalse(check_number('3+5'))
        self.assertFalse(check_number(''))

    def test_convert_rating(self):
        """ Test valid input within range """
        self.assertEqual(convert_rating('3.5', 1, 5), '3.5')
        self.assertEqual(convert_rating('1', 1, 5), '1.0')
        self.assertEqual(convert_rating('5', 1, 5), '5.0')

        """ Test valid input outside range """
        self.assertEqual(convert_rating('0.5', 1, 5), '1')
        self.assertEqual(convert_rating('10', 1, 5), '5')
