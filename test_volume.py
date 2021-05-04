import unittest
import volume

class TestCase (unittest.TestCase):
    def test_1(self):
        self.assertEqual(volume.volume("a"),1)

    def test_2(self):
        self.assertEqual(volume.volume(-2),1)

    def test_3(self):
        self.assertEqual(volume.volume(5),25) 

if __name__ == '__main__':
    unittest.main(verbosity=2)