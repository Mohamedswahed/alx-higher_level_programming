#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])"""
    def test_no_arg(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer(), None)

    def test_emp_lst(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([98]), 98)

    def test_iden(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_max_st(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([5, 4, 3, 2]), 5)

    def test_ord(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_ord_l(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]), 20)

    def test_unor(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_unor_l(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([23, 58, 91, 24, 1024, 89, 98,
                                     108, 256, 512]), 1024)

    def test_pos_and_negs(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer([-23, 58, 91, 24, -1024, 89, 98, 108, -256, -512]),
            108)

    def test_pos_and_negs_l(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [-6351, 9735, -8649, 4405, 6261, -1907, -9443, -6308,
                    7474, -2513, 5721, 2319, 74, 7946, -5544, 7693, -7013,
                    -6683, 715, -8738, 9678, -1081, 4730, -1376, 9126,
                    -9388, 8552, 3582, 3500, 7924, 211, -2976, 6346, -5405,
                    899, -3432, -2550, -3353, 6944, 9623]), 9823)

    def test_negs(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [-6105619, -854849, -562553, -3088955, -6711290, -4817844,
                    -1907189, -8110534, -6601769, -5837524, -4726702,
                    -7202853, -6891036, -4379807, -7955196, -1536591,
                    -2839083, -2586661, -9941097, -3136620]), -71562)

    def test_ints_and_flts(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [10, 99.8, -100, -0.1, 1000, 9999, -100000, 9998.9]), 9999)

    def test_ints_and_flts_l(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [199872.7619047619, 115249.8813559322, 37972.944444444445,
                    120549.90322580645, 30889.777777777777, 986136.4,
                    142333.11764705883, 199123.75]), 2503567)

    def test_flts(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer(
                [.00123, .457568, .02345, .23423434, .45675674, .678678,
                    .867090, .74653, .5745375]), 0.86709)

    def test_numeric_stg(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer("192834754"), "9")

    def test_stg(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer("Holberton"), "t")

    def test_lsts(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([[], [2], [4], [2, 9]]), [4])

    def test_str_lst(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(
            max_integer([["foo"], ["boo"], ["abc"], ["sic"], ["ric"]]),
            ["sic"])

    def test_inf(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([99, float('inf'), float('-inf')]),
                         float('inf'))

    def test_nan(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([99, float('nan'), 100]), 100)

    def test_mxd_list(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([[], [2], [4], [2, 9], 99, "foo"])

    def test_mxd_list_int_str(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([99, "foo"])

    def test_none(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_dict(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer([{20: 23, 14: 45}, {"a": "b"}])

    def test_int(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(98)

    def test_flt(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(9.8)

if __name__ == '__main__':
    unittest.main()
