# Z 字形变换

## 算法题

::: tip 题目
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

:::

~~~
示例1：
    输入: s = "LEETCODEISHIRING", numRows = 3
    输出: "LCIRETOESIIGEDHN"
~~~

~~~
示例2：
    输入: s = "LEETCODEISHIRING", numRows = 4
    输出: "LDREOEIIECIHNTSG"
    解释:
        L     D     R
        E   O E   I I
        E C   I H   N
        T     S     G
~~~

来源： &emsp; [力扣LeetCode](https://leetcode-cn.com/problems/zigzag-conversion)

## 解答过程

### 我的思路

暴力破解法：

经过观察，发现输入字符串 前 numRows 作为第一列， 其后 ( numRows - 2 ) 个字符串作为第二列

这样依次排列

所以我们可以模拟这个过程

先建立一个长度是 numRows 二维列表，来存储数据

:::tip 注意点
if total <= numRows or numRows == 1:
   return s
这个判断很重要
:::

### 源码

```python
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
```



::: warning python源码文件位于
/python/字符串操作/Z字形变换-2020-09-17.py
:::
