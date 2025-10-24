import unittest
from assign2 import func1


class TestFunc1(unittest.TestCase):
    def test_example_case(self):
        expected = "最遠弗利沙；最近丁滿、貝吉塔"
        actual = func1("辛巴")
        self.assertEqual(
            actual, expected, f"Input 辛巴: Expect {expected}, got {actual}"
        )

        expected = "最遠丁滿、弗利沙；最近特南克斯"
        actual = func1("悟空")
        self.assertEqual(
            actual, expected, f"Input 悟空: Expect {expected}, got {actual}"
        )

        expected = "最遠辛巴；最近特南克斯"
        actual = func1("弗利沙")
        self.assertEqual(
            actual, expected, f"Input 弗利沙 Expect {expected}, got {actual}"
        )

        expected = "最遠丁滿；最近悟空"
        actual = func1("特南克斯")
        self.assertEqual(
            actual, expected, f"Input 特南克斯: Expect {expected}, got {actual}"
        )


if __name__ == "__main__":
    unittest.main()
