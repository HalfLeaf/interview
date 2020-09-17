#-*-coding:utf-8-*-

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total = len(nums)
        i = 0
        j = 0
        result = 0
        while j < total:
            if nums[j] == 1:
                j = j + 1
            else:
                if i != j:
                    result = max(result, j - i)
                j = j + 1
                i = j
        result = max(result, j - i)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))