#-*-coding:utf-8-*-

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        total = len(s)
        p = 0
        self.result = []
        while (p+1) < total:
            for q in range(p+2, total+1):
                w = s[p:q]
                self.isSubset(w)
            p = p +1
        return len(self.result)

    def isSubset(self, s:str):
        total = len(s)
        if total%2 == 0:
            a = s[0:total//2]
            b = s[total//2:]
            c = "0"*(total//2)
            d = "1"*(total//2)
            if(a == c and b ==d) or (a==d and b ==c):
                self.result.append(s)







if __name__ == '__main__':
    s = Solution()
    result = s.countBinarySubstrings("00110011")
    print(result)
