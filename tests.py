import random
import unittest
from solution import Solution


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
                  ['0', '1', '1', '0', '0']
                  ['0', '1', '1', '0', '0']
                  ['0', '0', '0', '0', '0']]
        self.assertEqual(2, self.solution.maximal_square(matrix))

    def test_one_square_three_size(self):
        matrix = [['0', '0', '0', '0', '0'],
                  ['0', '1', '1', '1', '0']
                  ['0', '1', '1', '1', '0']
                  ['0', '1', '1', '1', '0']]
        self.assertEqual(3, self.solution.maximal_square(matrix))

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

    def test_wrong_matrix_shapes_then_throw_exception(self):
        matrix = [['0' for j in range(random.randint(1, 6))] for i in range(6)]
        with self.assertRaises(Exception) as exc:
            res = self.solution.maximal_square(matrix)
        self.assertEqual(str(exc.exception), 'Invalid matrix shapes')

    def test_wrong_values_then_throw_exception(self):
        matrix = [['0', '1', 1],
                  ['a', '0', 0]]
        with self.assertRaises(Exception) as exc:
            res = self.solution.maximal_square(matrix)
        self.assertEqual(str(exc.exception),'Invalid values, must be only "0" and "1"')



if __name__ == '__main__':
    unittest.main()