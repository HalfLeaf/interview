#-*-coding:utf-8-*-

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            for i,j in enumerate(nums):
                if j > target and i == 0:
                    return 0
                elif j < target and i+1 == len(nums):
                    return i+1
                elif j < target and nums[i+1] > target:
                    return i+1

if __name__ == '__main__':
    s = Solution()
    a = s.searchInsert( [1,3,5,6], 7)
    print(a)