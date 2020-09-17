#-*-coding:utf-8-*-

from typing import List

class Solution1:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        total = len(nums)
        for i in range(1, total+1):
            for j in range(0, total-i+1):
                if sum(nums[j:j+i]) >= s:
                    return i
        return 0

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        total = len(nums)
        result = total
        for i in range(0, total):
            if nums[i] >= s:
                return 1
            j = 1
            while i+j <= total:
                if sum(nums[i:j+i]) >= s:
                    result = min(result, j)
                j = j + 1
        if result == total:
            result = total if sum(nums) >= s else 0
        return result




if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(s = 7, nums = [2,3,1,2,4,3]))