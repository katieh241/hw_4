import unittest
import name

class TestCase (unittest.TestCase):
    def test_1(self):
        self.assertEqual(name.name("hi", 3), 1)

    def test_2(self):
        self.assertEqual(name.name(2, 4), 1)

    def test_3(self):
        self.assertEqual(name.name("Katie", "Holmes"), "Katie Holmes")

    def test_4(self):
        self.assertEqual(name.name("Katie","Holmes"), "KatieHolmes") 
    
if __name__ == '__main__':
    unittest.main(verbosity=2)