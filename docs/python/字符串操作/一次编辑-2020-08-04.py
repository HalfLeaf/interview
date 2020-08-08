#-*-coding:utf-8-*-

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        first_length = len(first)
        second_length = len(second)
        if abs(first_length - second_length) > 1:
            return False
        else:
            if first_length > second_length:
                # 删除
                flag = 0
                for i,v in enumerate(first):
                    try:
                        if v != second[i-flag]:
                            flag += 1
                    except:
                        pass
                    if flag > 1:
                        return False
                return True
            elif second_length > first_length:
                # 增加
                flag = 0
                for i,v in enumerate(second):
                    try:
                        if v != first[i-flag]:
                            flag += 1
                    except:
                        pass
                    if flag > 1:
                        return False
                return True
            else:
                # 替换
                flag = 0
                for i,v in enumerate(second):
                    if v != first[i]:
                        flag += 1
                    if flag > 1:
                        return False
                return True


if __name__ == '__main__':
    s = Solution()
    result = s.oneEditAway("islander","slander")
    print(result)
