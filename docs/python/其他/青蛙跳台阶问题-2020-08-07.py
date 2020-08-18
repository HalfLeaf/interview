#-*-coding:utf-8-*-

class Solution:
    def numWays(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007

if __name__ == '__main__':
    s = Solution()
    result = s.numWays(7)
    print(result)
