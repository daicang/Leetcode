
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        n = len(matrix)

        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        for i in range(n//2):
            for j in range(n):
                matrix[j][i], matrix[j][n-i-1] = matrix[j][n-i-1], matrix[j][i]
