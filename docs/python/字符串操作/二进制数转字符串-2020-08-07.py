#-*-coding:utf-8-*-

class Solution:
    def printBin(self, num: float) -> str:
        if 0 < num < 1:
            total = 0
            index = -1
            result = "0."
            while total < num:
                tmp = total + 2**index
                if tmp > num:
                    result += "0"
                    index = index - 1
                else:
                    total = tmp
                    result += "1"
                    index = index - 1
                if len(result) >32:
                    return "ERROR"
            return result
        else:
            return "ERROR"



if __name__ == '__main__':
    s = Solution()
    result = s.printBin(0.1)
    print(result)
