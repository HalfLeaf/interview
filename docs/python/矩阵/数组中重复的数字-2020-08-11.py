#-*-coding:utf-8-*-

from typing import List
from collections import Counter

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        s = Counter(nums)
        result = [x for x, y in s.items() if y > 1]
        return result[0]


if __name__ == '__main__':
    s = Solution()
    s.findRepeatNumber([2, 3, 1, 0, 2, 5, 3])