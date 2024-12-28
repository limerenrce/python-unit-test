import unittest
from src.algorithms.quick_sort import quick_sort


class TestQuickSort(unittest.TestCase):
    def setUp(self):
        print("\nStarting a new quick sort test case ...")

    def tearDown(self):
        print("Test case finished \n")

    def test_normal_array(self):
        self.assertEqual(quick_sort([9, 1, 5, 2, 3]), [1, 2, 3, 5, 9])

    #  Arrays that are already sorted.
    def test_sorted_array(self):
        self.assertEqual(quick_sort([1, 2, 3]), [1, 2, 3])

    #  Reversed arrays.
    def test_reverse_array(self):
        self.assertEqual(quick_sort([9, 8, 7, 6, 5]), [5, 6, 7, 8, 9])

    #  Arrays with identical elements.
    def test_identical_elements(self):
        self.assertEqual(quick_sort([5, 5, 5, 5]), [5, 5, 5, 5])

    def test_empty_array(self):
        self.assertEqual(quick_sort([]), [])

    def test_single_element(self):
        self.assertEqual(quick_sort([42]), [42])


if __name__ == "__main__":
    unittest.main()
