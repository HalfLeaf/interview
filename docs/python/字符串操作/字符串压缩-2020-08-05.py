#-*-coding:utf-8-*-

class Solution:
    def compressString(self, S: str) -> str:
        if not S: return S
        result = S[0]
        current = S[0]
        count = 1
        for s in S[1:]:
            if s == current:
                count += 1
            else:
                current = s
                result += f"{count}{current}"
                count = 1
        result += f"{count}"
        return result if len(S) > len(result) else S




if __name__ == '__main__':
    s = Solution()
    result = s.compressString("aabcccccaaa")
    print(result)
