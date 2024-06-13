import unittest
from Ten import mergesort, insertionsort, get_data, LEN_INPUT_LIST
import time
class TestTwoAlghoritms(unittest.TestCase):
    def test_valid_data_of_two(self):
        data = get_data(LEN_INPUT_LIST)
        self.assertEqual(mergesort(data), insertionsort(data)) 


if __name__ == '__main__':
    unittest.main()