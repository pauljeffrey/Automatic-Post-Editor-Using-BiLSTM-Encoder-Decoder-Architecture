import json
import sys
import unittest
sys.path.append("..")
from algo.repeated_str_with_matrix import RepeatedStrWithMatrix  # noqa


class TestMatrix(unittest.TestCase):
    def test(self):
        with open('./test_matrix_cases.json', 'r', encoding='utf8') as f:
            dict = json.load(f)
            cases = dict['cases']

            for case in cases:
                org_str = case['org_str']
                cmp_str = case['cmp_str']
                expected = case['expected']

                inst = RepeatedStrWithMatrix(org_str, cmp_str)
                res = inst.get_res()
                repeated_str_len = res['repeated_str_len']

                self.assertEqual(repeated_str_len, expected)


if __name__ == "__main__":
    unittest.main()
