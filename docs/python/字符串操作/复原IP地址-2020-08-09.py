#-*-coding:utf-8-*-
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        total = len(s)
        self.result = []
        if total < 4 or total > 12:
            return []
        for i in range(1, 4):
            first = s[:i]
            for j in range(1, 4):
                if (i+j) > total:
                    break
                second = s[i:(i+j)]
                for m in range(1, 4):
                    if (i+j+m) > total:
                        break
                    third = s[(i+j):(i+j+m)]
                    for n in range(1, 4):
                        if (i+j+m+n) > total:
                            break
                        fourth = s[(i+j+m):(i+j+m+n)]
                        if (i+j+m+n) == total:
                            self.isValid([first, second, third, fourth])

        return self.result

    def isValid(self, s:List[str]):
        for i in s:
            if (i.startswith("0") and len(i)> 1 ) or int(i) > 255:
                break
        else:
            self.result.append(".".join(s))



if __name__ == '__main__':
    s = Solution()
    result = s.restoreIpAddresses("010010")
    print(result)
