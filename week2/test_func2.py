import unittest
from assign2 import func2


class TestFunc2(unittest.TestCase):
    def test_example_case(self):
        expected = "S3"
        actual = func2(services, 15, 17, "c>=800")
        self.assertEqual(
            actual,
            expected,
            f'Input services, 15, 17, "c>=800": Expect {expected}, got {actual}',
        )

        expected = "S3"
        actual = func2(services, 11, 13, "r<=4")
        self.assertEqual(
            actual,
            expected,
            f'Input services, 11, 13, "r<=4": Expect {expected}, got {actual}',
        )

        expected = "Sorry"
        actual = func2(services, 10, 12, "name=S3")
        self.assertEqual(
            actual,
            expected,
            f'Input services, 10, 12, "name=S3": Expect {expected}, got {actual}',
        )

        expected = "S1"
        actual = func2(services, 15, 18, "r>=4.5")
        self.assertEqual(
            actual,
            expected,
            f'Input services, 15, 18, "r>=4.5": Expect {expected}, got {actual}',
        )

        expected = "Sorry"
        actual = func2(services, 16, 18, "r>=4")
        self.assertEqual(
            actual,
            expected,
            f'Input services, 16, 18, "r>=4": Expect {expected}, got {actual}',
        )

        expected = "Sorry"
        actual = func2(services, 13, 17, "name=S1")
        self.assertEqual(
            actual,
            expected,
            f'Input services, 13, 17, "name=S1": Expect {expected}, got {actual}',
        )

        expected = "S2"
        actual = func2(services, 8, 9, "c<=1500")
        self.assertEqual(
            actual,
            expected,
            f'Input services, 8, 9, "c<=1500": Expect {expected}, got {actual}',
        )

        expected = "S1"
        actual = func2(services, 8, 9, "c<=1500")
        self.assertEqual(
            actual,
            expected,
            f'Input services, 8, 9, "c<=1500": Expect {expected}, got {actual}',
        )

        expected = "S3"
        actual = func2(services, 8, 9, "c<=1500")
        self.assertEqual(
            actual,
            expected,
            f'Input services, 8, 9, "c<=1500": Expect {expected}, got {actual}',
        )

        expected = "Sorry"
        actual = func2(services, 8, 9, "c<=1500")
        self.assertEqual(
            actual,
            expected,
            f'Input services, 8, 9, "c<=1500": Expect {expected}, got {actual}',
        )

services = [
    {"name": "S1", "r": 4.5, "c": 1000},
    {"name": "S2", "r": 3, "c": 1200},
    {"name": "S3", "r": 3.8, "c": 800},
]


if __name__ == "__main__":
    unittest.main()
