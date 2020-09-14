#-*-coding:utf-8-*-

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = [len(x) for x in strs]
        min_str = strs[length.index(min(length))]
        result = ""
        for i in range(len(min_str)):
            flag = 1
            for s in strs:
                if s[i] != min_str[i]:
                    break
            else:
                result = f"{result}{min_str[i]}"
                flag = 0
            if flag:
                break
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flerkfight"]))