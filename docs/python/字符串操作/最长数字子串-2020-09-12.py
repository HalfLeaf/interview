# -*-coding:utf-8-*-

import re

def get_max_string(s: str) -> int:
    result = ""
    tmp = ""
    for index, single in enumerate(s):
        if re.search(r"[0-9]", single):
            tmp = f"{tmp}{single}"
        else:
            if len(tmp) >= len(result):
                result = tmp
            tmp = ""

    if len(tmp) >= len(result):
        result = tmp

    print("".join(result))
    print(len(result))
    return len(result)


if __name__ == '__main__':
    get_max_string("abcdabc")