# 最长数字子串

## 华为面试真题

::: tip 题目
在字符串中找出连续最长的数字串

要求:

1. 相同长度的数字串，取最后一组数字串
2. 返回最长的数字串长度

:::

~~~
示例1：
 输入：abcd1234abc12345
 输出：12345, 5
~~~

~~~
示例2：
 输入：abcd1234abc6789
 输出：6789, 4
~~~

来源： &emsp; 华为面试真题，来源怀疑是 牛客网

## 解答过程

### 我的思路

遍历整个字符串，找到数字存入临时数字串，当前的数字串与上次存储的数字串进行长度比较，

如果当前的数字串长度大于等于上次存储的数字串长度，当前数字串替换上次存储值


### 源码

```python
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
```

面试官看着写的，有点紧张，用时5分钟，用的方法有点土

::: warning python源码文件位于
/python/字符串操作/最长数字子串-2020-09-12.py
:::
