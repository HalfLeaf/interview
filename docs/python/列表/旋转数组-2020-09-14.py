#-*-coding:utf-8-*-

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for index, num in enumerate(nums):
            if sum(nums[:index]) == sum(nums[index+1:]):
                return index
        return -1


if __name__ == '__main__':
    s = Solution()
    s.pivotIndex([1, 7, 3, 6, 5, 6])