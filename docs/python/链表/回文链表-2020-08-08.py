#-*-coding:utf-8-*-

from typing import List
from copy import deepcopy

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        if row:
            tmp = deepcopy(matrix)
            col = len(matrix[0])
            for i in range(row):
                for j in range(col):
                    if tmp[i][j] == 0:
                        for m in range(col):
                            matrix[i][m] = 0
                        for n in range(row):
                            matrix[n][j] = 0
            print(matrix)


if __name__ == '__main__':
    s = Solution()
    s.setZeroes(matrix = [
      [1,1,1],
      [1,0,1],
      [1,1,1]
    ])