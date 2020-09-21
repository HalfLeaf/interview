#-*-coding:utf-8-*-

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        buy = None
        for i in range(len(prices) - 1):
            if buy is None and prices[i+1] > prices[i]:
                buy = prices[i]
            if not buy is None and prices[i] > prices[i+1]:
                result += prices[i] - buy
                buy = None
        if not buy is None:
            result += prices[-1] - buy
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([2,1,2,0,1]))