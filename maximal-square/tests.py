import random
import unittest
from solution import Solution, Solution2


class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_no_squares(self):
        matrix = [['0', '0', '0'],
                  ['0', '0', '0']]
        self.assertEqual(0, self.solution.maximal_square(matrix))

    def test_onepoint_square(self):
        matrix = [['0', '1', '0'],
                  ['0', '0', '0']]
        self.assertEqual(1, self.solution.maximal_square(matrix))

    def test_one_square_two_size(self):
        matrix = [['0', '0', '0', '0', '0'],
                  ['0', '1', '1', '0', '0'],
                  ['0', '1', '1', '0', '0'],
                  ['0', '0', '0', '0', '0']]
        self.assertEqual(2, self.solution.maximal_square(matrix))

    def test_two_squares_two_size(self):
        matrix = [['0', '0', '0', '0', '0'],
                  ['0', '1', '1', '1', '0'],
                  ['0', '1', '1', '1', '0'],
                  ['0', '0', '0', '0', '0']]
        self.assertEqual(2, self.solution.maximal_square(matrix))

    def test_one_square_not_filled(self):
        matrix = [['0', '0', '0', '0', '0'],
                  ['0', '1', '1', '0', '0'],
                  ['0', '1', '0', '0', '0'],
                  ['0', '0', '0', '0', '0']]
        self.assertEqual(1, self.solution.maximal_square(matrix))

    def test_one_square_three_size(self):
        matrix = [['0', '0', '0', '0', '0'],
                  ['0', '1', '1', '1', '0'],
                  ['0', '1', '1', '1', '0'],
                  ['0', '1', '1', '1', '0']]
        self.assertEqual(3, self.solution.maximal_square(matrix))

    def test_one_square_three_size_with_zero_at_center(self):
        matrix = [['1', '1', '1'],
                  ['1', '0', '1'],
                  ['1', '1', '1']]
        self.assertEqual(1, self.solution.maximal_square(matrix))

    def test_filled_matrix_square_four_size(self):
        matrix = [['1', '1', '1', '1'],
                  ['1', '1', '1', '1'],
                  ['1', '1', '1', '1'],
                  ['1', '1', '1', '1']]
        self.assertEqual(4, self.solution.maximal_square(matrix))

    def test_empty_matrix_then_throw_exception(self):
        matrix = []
        with self.assertRaises(Exception) as exc:
            res = self.solution.maximal_square(matrix)
        self.assertEqual(str(exc.exception), 'Invalid matrix size')

    def test_big_matrix_then_throw_exception(self):
        matrix = [['0' for j in range(301)] for i in range(301)]
        with self.assertRaises(Exception) as exc:
            res = self.solution.maximal_square(matrix)
        self.assertEqual(str(exc.exception), 'Invalid matrix size')

    def test_invalid_matrix_shapes_then_throw_exception(self):
        matrix = [['0' for j in range(random.randint(1, 6))] for i in range(6)]
        with self.assertRaises(Exception) as exc:
            res = self.solution.maximal_square(matrix)
        self.assertEqual(str(exc.exception), 'Invalid matrix shapes')

    def test_invalid_values_literals_then_throw_exception(self):
        matrix = [['b', 'd', 'r'],
                  ['a', '0', 'a']]
        with self.assertRaises(Exception) as exc:
            res = self.solution.maximal_square(matrix)
        self.assertEqual(str(exc.exception),'Invalid values, matrix must contain only "0" and "1"')

    def test_invalid_int_values_then_throw_exception_(self):
        matrix = [[0, 1, 1],
                  [1, 0, 0]]
        with self.assertRaises(Exception) as exc:
            res = self.solution.maximal_square(matrix)
        self.assertEqual(str(exc.exception),'Invalid values, matrix must contain only "0" and "1"')


if __name__ == '__main__':
    unittest.main()
