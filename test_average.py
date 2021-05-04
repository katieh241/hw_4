import unittest
import average

class TestCase (unittest.TestCase):
    def test_1(self):
        self.assertEqual(average.average({1, 2, 3, 4}), 2)

    def test_2(self):
        self.assertEqual(average.average({}), 1)

    def test_3(self):
        self.assertEqual(average.average({12, 3, 5}), 7)

if __name__ == '__main__':
    unittest.main(verbosity=2)