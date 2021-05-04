import unittest
import name

class TestCase (unittest.TestCase):
    def test_1(self):
        self.assertEqual(name.name("hi", "hi"),"hi hi")

    def test_2(self):
        self.assertEqual(name.name("hi", "hi"),"hi hi")

    def test_3(self):
        self.assertEqual(name.name("hi", "hi"), "hi hi")
    
if __name__ == '__main__':
    unittest.main(verbosity=2)