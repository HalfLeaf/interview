#-*-coding:utf-8-*-

from typing import List

class Solution1:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        max_value = None
        min_value = None
        if not intervals:
            return []
        for index, single in enumerate(intervals):
            print(single, min_value, max_value)
            if min_value is None:
                min_value = single[0]
                max_value = single[1]
            elif min_value <= single[0] <= max_value or \
                 min_value <= single[1] <= max_value or \
                 single[0] <= min_value <= single[1] or \
                 single[0] <= max_value <= single[1]:
                min_value = min(min_value, single[0])
                max_value = max(max_value, single[1])
            else:
                result.append([min_value, max_value])
                min_value = single[0]
                max_value = single[1]
        result.append([min_value, max_value])
        return result

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        max_value = None
        min_value = None
        if not intervals:
            return []
        total = len(intervals)
        a = None
        b = None
        for index, single in enumerate(intervals):
            if a is None:
                a = single[0]
                b = single[1]
            for i in range(index, total):
                if min_value is None:
                    min_value = intervals[i][0]
                    max_value = intervals[i][1]
                elif min_value <= intervals[i][0] <= max_value or \
                     min_value <= intervals[i][1] <= max_value or \
                     intervals[i][0] <= min_value <= intervals[i][1] or \
                     intervals[i][0] <= max_value <= intervals[i][1]:
                    min_value = min(min_value, intervals[i][0])
                    max_value = max(max_value, intervals[i][1])
            if min_value <= a <= max_value or \
               min_value <= b <= max_value or \
               a <= min_value <= b or \
               a <= max_value <= b:
                a = min(min_value, a)
                b = max(max_value, b)
                min_value = None
                max_value = None
            else:
                result.append([a, b])
                min_value = None
                max_value = None
                a = single[0]
                b = single[1]
        result.append([a, b])
        return result




if __name__ == '__main__':
    s = Solution()
    a = s.merge([[1,3],[4,5],[6,8], [1, 10]])
    print(a)