from typing import List


class Solution:

    def maximal_square(self, matrix: List[List[str]]) -> int:
        '''
        Get maximal square size, that contains only "1"
        :param matrix: matrix of "0" and "1", matrix sizes are 1 <= n, m <= 300
        :return: size of the largest square
        '''
        self._validate(matrix)
        return self._maximal_square(matrix)

    def _maximal_square(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        max_square = 0
        tmp = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or matrix[i][j] == '0':
                    tmp[i][j] = int(matrix[i][j])
                else:
                    tmp[i][j] = min(tmp[i][j - 1],
                                    tmp[i - 1][j - 1],
                                    tmp[i - 1][j]) + int(matrix[i][j])
                if tmp[i][j] > max_square:
                    max_square = tmp[i][j]
        return max_square

    def _validate(self, matrix):
        self._check_shapes(matrix)
        self._check_values(matrix)

    def _check_shapes(self, matrix):
        m = len(matrix)
        if m < 1 or m > 300:
            raise Exception('Invalid matrix size')
        else:
            n = len(matrix[0])
            if n < 1 or n > 300:
                raise Exception('Invalid matrix size')
            else:
                for i in range(1, m):
                    if n != len(matrix[i]):
                        raise Exception('Invalid matrix shapes')

    def _check_values(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                el = matrix[i][j]
                if el != '0' and el != '1':
                    raise Exception('Invalid values, matrix must contain only "0" and "1"')


class Solution2(Solution):

    def _maximal_square(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        max_square = 0
        tmp = [[0 for j in range(n)] for i in range(2)]

        for i in range(m):
            for j in range(n):
                if i == 0 or matrix[i][j] == '0':
                    tmp[0][j] = int(matrix[i][j])
                elif j == 0 or matrix[i][j] == '0':
                    tmp[1][j] = int(matrix[i][j])
                else:
                    tmp[1][j] = min(tmp[1][j - 1],
                                    tmp[0][j - 1],
                                    tmp[0][j]) + int(matrix[i][j])
                if i == 0:
                    if tmp[0][j] > max_square:
                        max_square = tmp[0][j]
                else:
                    if tmp[1][j] > max_square:
                        max_square = tmp[1][j]
            if i != 0:
                tmp[0], tmp[1] = tmp[1], tmp[0]
        return max_square
