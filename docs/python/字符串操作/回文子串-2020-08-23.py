#-*-coding:utf-8-*-

class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s: return 0
        total = len(s)
        result = total
        for i in range(total-1):
            for j in range(i+2, total+1):
                if self.isPalindrome(s[i:j]):
                    result = result + 1
        return result

    def isPalindrome(self, s:str):
        t = len(s)
        t = t-1 if t%2 else t
        for i in range(0, t//2+1):
            if s[i] != s[-i-1]:
                return False
        return True





if __name__ == '__main__':
    s = Solution()
    result = s.countSubstrings("aaa")
    print(result)
