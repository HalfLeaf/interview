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
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= s:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1

        return 0 if ans == n + 1 else ans



if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(s = 7, nums = [2,3,1,2,4,3]))