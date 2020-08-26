#-*-coding:utf-8-*-

from typing import List
import itertools
class Solution:
    def permutation(self, ss: str) -> List[str]:
        if not ss:
            return []
        return sorted(list(set(map(''.join, itertools.permutations(ss)))))


if __name__ == '__main__':
    s = Solution()
    result = s.permutation("abc")
    print(result)
