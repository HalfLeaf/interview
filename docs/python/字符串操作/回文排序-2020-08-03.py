#-*-coding:utf-8-*-

from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        """
            借助counter直接计数
            counter返回的是字典类型，值是出现次数
            奇数只有0个或1个可以达到回文效果
        """
        c = Counter(s)
        result = 0
        for v in c.values():
            if v % 2:
                result += 1
            if result > 1:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    result = s.canPermutePalindrome("tactcoa")
    print(result)
