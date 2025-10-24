import unittest
from assign2 import func3


# inherit from unittest.TestCase
class TestFunc3(unittest.TestCase):
    # Test method must start with 'test_'
    def test_example_case(self):
        # 1. Test case: func3(1) should return 23
        expected = 23
        actual = func3(1)
        # Use assertion method to check is expect result equals to actual result
        self.assertEqual(actual, expected, f"input 1: Expect {expected}, got {actual}")

        # 2. Test case: func3(5) should return 21
        expected = 21
        actual = func3(5)
        self.assertEqual(actual, expected, f"input 5: Expect {expected}, got {actual}")

        # 3. Test case: func3(10)) should return 16
        expected = 16
        actual = func3(10)
        self.assertEqual(actual, expected, f"input 10: Expect {expected}, got {actual}")

        # 4. Test case: func3(30)) should return 6
        expected = 6
        actual = func3(30)
        self.assertEqual(actual, expected, f"input 30: Expect {expected}, got {actual}")
    
    # Adding a few more edge cases:
    def test_cycle_boundaries(self):
        # Test the end of a full cycle (index 4)
        self.assertEqual(func3(4), 23, "Input 4 (end of cycle 1)")
        # Test the start of a new cycle (index 5, which is already in the first test)
        
        # Test the end of the second cycle (index 8)
        # 25 + 2*(-2) = 21
        self.assertEqual(func3(8), 21, "Input 8 (end of cycle 2)")

    def test_mid_cycle_values(self):
        # index 2: 25 + 0*(-2) + (-5) = 20
        self.assertEqual(func3(2), 20, "Input 2") 
        # index 3: 25 + 0*(-2) + (-4) = 21
        self.assertEqual(func3(3), 21, "Input 3") 
        # index 6: 25 + 1*(-2) + (-5) = 18
        self.assertEqual(func3(6), 18, "Input 6")


# This block allows the file to be run directly to execute the tests
if __name__ == "__main__":
    unittest.main()
