#-*-coding:utf-8-*-

from typing import List,Dict

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        result = []
        direction = 1  # 遍历方向  1 -- 向上  0 -- 向下
        col = len(matrix)
        row = len(matrix[0])
        i = 0
        j = 0
        while 0 <= j < col and 0 <= i < row:
            print('start', i, j)
            result.append(matrix[i][j])
            if direction:
                if j == col - 1:
                    i = i + 1
                else:
                    i = i - 1
                    j = j + 1
            else:
                i = i + 1
                j = j - 1
            print('middle', i, j)
            if not 0 <= j < col:
                direction = 1
                j = j + 1
            if not 0 <= i < row:
                direction = 0
                i = i + 1
            print('end',  i, j)
        print(result)


if __name__ == '__main__':
    s = Solution()
    print(s.findDiagonalOrder([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [4,5,6,7,8], [5,6,7,8,9]]))