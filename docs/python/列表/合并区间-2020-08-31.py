#-*-coding:utf-8-*-

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        max_value = None
        min_value = None
        for single in intervals:
            flag = 0
            for one in single:
                if min_value and max_value and min_value <= one <= max_value:
                    flag = 1
                if max_value is None:
                    max_value = one
                elif min_value is None:
                    min_value = one
                if min_value and min_value > max_value:
                    min_value, max_value = max_value, min_value
                if flag:
                    max_value = max(max_value, one)
                    result.append([min_value, max_value])
                    min_value = None
                    max_value = None
        return result




if __name__ == '__main__':
    s = Solution()
    a = s.merge([[1,4],[4,5]])
    print(a)