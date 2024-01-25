# test_hello.py
import unittest
from hello import main

class TestHello(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), "Hello")

