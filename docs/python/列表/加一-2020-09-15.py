#-*-coding:utf-8-*-

from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return []
        a = digits[-1]
        if a == 9:
            for i in range(len(digits)-1, -1, -1):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    break
                if i == 0:
                    digits.insert(0, 1)
        else:
            digits[-1] = a + 1
        return digits


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([9,9,9,9]))