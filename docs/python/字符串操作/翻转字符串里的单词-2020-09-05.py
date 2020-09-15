# -*-coding:utf-8-*-

import re

class Solution:
    def reverseWords(self, s: str) -> str:
        s = re.sub(r' +', " ", s.strip()).split(" ")
        s.reverse()
        return " ".join(s)


if __name__ == '__main__':
    s = Solution()
    print(s.reverseWords("  hello       world!  "))