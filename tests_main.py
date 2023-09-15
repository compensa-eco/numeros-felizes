import unittest
# função que receba um inteiro e retorne um bool
from main import is_happy, calc_pow, map_number, sum_digits_calculated


class TestHappyFunction(unittest.TestCase):

    def test_function_happy(self):
        num = 7
        number_is_happy = is_happy(num)
        self.assertTrue(number_is_happy)

    def test_return_false_if_input_is_not_int(self):
        num = 7.5
        number_is_happy = is_happy(num)
        self.assertFalse(number_is_happy)

    def test_one_digit_pow_result(self):
        num = 7
        result_pow = calc_pow(num)
        self.assertEqual(result_pow, 49)

    def test_map_string_to_array_number(self):
        string = '49'
        result = map_number(string)
        self.assertEqual(result, [4, 9])

    def test_sum_digits_calculated(self):
        string = '49'
        result = map_number(string)
        total = sum_digits_calculated(result)
        self.assertEqual(total, 97)


if __name__ == '__main__':
    unittest.main()
