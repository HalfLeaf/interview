# -*-coding:utf-8-*-

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        total = len(s)
        if total <= numRows or numRows == 1:
            return s
        result = []
        for i in range(numRows):
            result.append([])
        i = 0
        while i < total:
            for j, v in enumerate(s[i:i+(numRows)]):
                result[j].append(v)
            for m, v in enumerate(s[i+(numRows):(i+(numRows)+numRows-2)]):
                result[numRows-2-m].append(v)
            i = i +(numRows)+numRows-2
        tmp = ""
        for res in result:
            tmp = f"{tmp}{''.join(res)}"
        return tmp





if __name__ == '__main__':
    s = Solution()
    print(s.convert(s = "AB", numRows = 1))