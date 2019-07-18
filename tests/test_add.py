import unittest
from code.add import add

class AddTestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(add(1,1),3, "oops ur shit")

    def test_two(self):
        self.assertNotEqual(add(1,2),4)

    def test_three(self):
        self.assertEqual(add(1,1),2)

if __name__ == "__main__":
    unittest.main()
