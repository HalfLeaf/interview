#-*-coding:utf-8-*-

from typing import List
from copy import deepcopy

class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if i == n:
                return n
        return -1


if __name__ == '__main__':
    s = Solution()
    s.findMagicIndex(nums = [0, 2, 3, 4, 5])