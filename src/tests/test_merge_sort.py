import unittest
from src.algorithms.merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):
    def setUp(self):
        print("\nStarting a new merge sort test case ...")

    def tearDown(self):
        print("Test case finished \n")

    def test_normal_array(self):
        self.assertEqual(merge_sort([1, 7, 4, 8, 3]), [1, 3, 4, 7, 8])

    #  Arrays that are already sorted.
    def test_sorted_array(self):
        self.assertEqual(merge_sort([1, 2, 3]), [1, 2, 3])

    #  Reversed arrays.
    def test_reverse_array(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    #  Arrays with identical elements.
    def test_identical_elements(self):
        self.assertEqual(merge_sort([7, 7, 7]), [7, 7, 7])

    def test_empty_array(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element(self):
        self.assertEqual(merge_sort([10]), [10])


if __name__ == "__main__":
    unittest.main()
