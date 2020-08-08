#-*-coding:utf-8-*-

from typing import List
import numpy as np

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rank = len(matrix)
        for i in range(rank):
            for j in range(i, rank, 1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(rank):
            matrix[i].reverse()


    def rotate1(self, matrix: List[List[int]]) -> None:
        rank = len(matrix)
        m = np.array(matrix, int)
        matrix = np.rot90(m, rank).tolist()
