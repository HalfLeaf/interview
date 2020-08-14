#-*-coding:utf-8-*-

class Solution:
    def isValid(self, S: str) -> bool:
        q = []
        d = {"{":"}", "[":"]", "(":")"}
        for x in S:
            if x in d.keys():
                q.append(x)
            elif q:
                prev = q.pop()
                for k,v in d.items():
                    if v == x:
                        if prev != k:
                            return False
            else:
                return False
        return False if q else True




if __name__ == '__main__':
    s = Solution()
    result = s.isValid("(]")
    print(result)
