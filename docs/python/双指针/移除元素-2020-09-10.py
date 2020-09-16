#-*-coding:utf-8-*-

from typing import List,Dict

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            if val in nums:
                nums.remove(val)
            else:
                break
        return len(nums)

if __name__ == '__main__':
    s = Solution()
    print(s.removeElement(nums = [2,2,3,2], val = 2))