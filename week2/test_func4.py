import unittest
from assign2 import func4


class TestFunc4(unittest.TestCase):

    def test_example_case(self):
        expected = 5
        actual = func4([3, 1, 5, 4, 3, 2], "101000", 2)
        self.assertEqual(
            actual,
            expected,
            f'Input [3, 1, 5, 4, 3, 2], "101000", 2: Expect {expected}, got {actual}',
        )

        expected = 4
        actual = func4([1, 0, 5, 1, 3], "10100", 4)
        self.assertEqual(
            actual,
            expected,
            f'Input [1, 0, 5, 1, 3], "10100", 4: Expect {expected}, got {actual}',
        )

        expected = 2
        actual = func4([4, 6, 5, 8], "1000", 4)
        self.assertEqual(
            actual,
            expected,
            f'Input [4, 6, 5, 8], "1000", 4: Expect {expected}, got {actual}',
        )

        # --- Edge Case Tests ---

    def test_nearest_greater_vs_perfect(self):
        # Priority check: Perfect match (3) is found first, even if a greater car (4) is available later.
        sp = [3, 4, 5, 2]
        stat = "0000"
        n = 3
        expected = 0
        actual = func4(sp, stat, n)
        self.assertEqual(actual, expected)

    def test_nearest_greater_minimum(self):
        # Nearest greater (minimum over-capacity) check: n=5, available: 10, 8, 6. Must pick 6 (index 2).
        sp = [10, 8, 6, 1]
        stat = "0000"
        n = 5
        expected = 2
        actual = func4(sp, stat, n)
        self.assertEqual(actual, expected)

    def test_nearest_less_maximum(self):
        # Nearest less (maximum under-capacity) check: n=5, available: 1, 3, 4. Must pick 4 (index 2).
        sp = [1, 3, 4, 10]
        stat = "0001"  # Ignore 10
        n = 5
        expected = 2
        actual = func4(sp, stat, n)
        self.assertEqual(actual, expected)

    def test_all_unavailable(self):
        # Availability check: All cars are busy ('1').
        sp = [3, 4, 5]
        stat = "111"
        n = 3
        expected = "Error"
        actual = func4(sp, stat, n)
        self.assertEqual(actual, expected)

    def test_empty_lists(self):
        # Boundary check: Empty lists for sp and stat.
        sp = []
        stat = ""
        n = 1
        expected = "Error"
        actual = func4(sp, stat, n)
        self.assertEqual(actual, expected)

    # --- Invalid Case Tests ---

    def test_sp_shorter_than_stat(self):
        # sp (length 2) is shorter than stat (length 3).
        sp = [1, 2]     
        stat = "000"    
        n = 1
        
        # Assert that the new defensive code correctly raises a ValueError
        with self.assertRaises(ValueError):
            func4(sp, stat, n)

    def test_input_n_is_zero(self):
        # n=0 is an unlikely group size, but should be tested.
        sp = [3, 4, 5]
        stat = "000"
        n = 0
        # In this case, 3 is the nearest greater, so index 0 is returned
        expected = 0
        actual = func4(sp, stat, n)
        self.assertEqual(actual, expected)

    def test_input_capacity_is_zero(self):
        # n=2, cars are [5, 0, 10]. Both 5 and 10 are greater, and 0 is less.
        # Priority rule dictates returning the 'Nearest Greater' (index 0) before 'Nearest Less'.
        sp = [5, 0, 10]
        stat = "000"
        n = 2

        # The nearest greater car is 5 (index 0).
        expected = 0
        actual = func4(sp, stat, n)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
