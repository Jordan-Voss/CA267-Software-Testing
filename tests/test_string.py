import unittest
from code.string import string,get

class AddTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(string('Hello'),'Hello')


if __name__ == "__main__":
    unittest.main()
