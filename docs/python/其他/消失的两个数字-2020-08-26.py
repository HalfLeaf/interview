#-*-coding:utf-8-*-
from typing import List

class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        result = []
        nums = sorted(nums)
        if nums[0] >1:
            result.append(1)
        if nums[0] >2:
            result.append(2)
        for i in range(1, len(nums)):
            if len(result) == 2:
                return result
            if nums[i] - nums[i - 1] != 1:
                result.append(nums[i]-1)
        if len(result) == 0:
            return [nums[-1]+1, nums[-1]+2]
        elif len(result) == 1:
            result.append(nums[-1]+1)
        return result


if __name__ == '__main__':
    s = Solution()
    result = s.missingTwo([1, 2, 3, 4, 6, 7, 9, 10])
    print(result)
