# -*-coding:utf-8-*-

class Solution1:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        total = len(s)
        if total < 2:
            return s
        for i in range(total-1):
            if not result: result = s[i]
            for j in range(i+len(result), total):
                sub = s[i:j+1]
                result = self.is_palindrome(result, sub)
        return result

    def is_palindrome(self, result: str, sub: str) -> str:
        total = len(sub)
        for i in range(len(sub) // 2):
            if sub[i] != sub[total-i-1]:
                break
        else:
            return result if len(result) > len(sub) else sub
        return result

class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("a"))