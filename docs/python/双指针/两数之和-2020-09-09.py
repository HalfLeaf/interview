#-*-coding:utf-8-*-

from typing import List,Dict

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        if len(nums) % 2:
            return 0
        nums = sorted(nums)
        return sum([x for i,x in enumerate(nums) if i%2==0])


if __name__ == '__main__':
    s = Solution()
    print(s.arrayPairSum([1,4,3,2]))