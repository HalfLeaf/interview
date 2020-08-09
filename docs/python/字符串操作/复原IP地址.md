#  复原IP地址

##  算法题

::: tip 题目
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。
:::

~~~
示例1：
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
~~~


来源： &emsp; [力扣LeetCode](https://leetcode-cn.com/problems/restore-ip-addresses)


##  解答过程

### 我的思路

暴力美学:

一个IP值只能是 0 ~ 255范围内，所有最多有3个字符

遍历出所有可能，然后一一剔除，不合理的值


```python
#-*-coding:utf-8-*-
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        total = len(s)
        self.result = []
        if total < 4 or total > 12:
            return []
        for i in range(1, 4):
            first = s[:i]
            for j in range(1, 4):
                if (i+j) > total:
                    break
                second = s[i:(i+j)]
                for m in range(1, 4):
                    if (i+j+m) > total:
                        break
                    third = s[(i+j):(i+j+m)]
                    for n in range(1, 4):
                        if (i+j+m+n) > total:
                            break
                        fourth = s[(i+j+m):(i+j+m+n)]
                        if (i+j+m+n) == total:
                            self.isValid([first, second, third, fourth])

        return self.result

    def isValid(self, s:List[str]):
        for i in s:
            if (i.startswith("0") and len(i)> 1 ) or int(i) > 255:
                break
        else:
            self.result.append(".".join(s))
```

* 耗时 60 ms
* 内存 13.8 MB

::: danger 注意点
IP值中对于0的处理，要注意一下，不能是在首字符的多个字符串
:::

### 优化改进

<span style="color:#42b983"> 从方法上来看，可以用递归来获取结果，从而降低代码的行数，整个时间复杂度应该没降 </span>


::: warning python源码文件位于
/python/字符串操作/复原IP地址-2020-08-09.py
:::



##  大佬解法


::: tip 解法1
深度优先搜索

定义DFS函数，查找在[0,255]之间的数字，然后再查找下一层
:::

* 耗时 36 ms
* 内存 13.7 MB


```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        # 定义查找符合条件的数字个数
        NUM = 4

        def _dfs(start, path):
            # 结束条件
            if len(path) > NUM or (len(path) == NUM and start < len(s) - 1):
                return
            # 追加结果
            if start >= len(s):
                if len(path) == NUM:
                    ans.append('.'.join(path))
                return

            # 当前是0, 特殊情况处理
            if s[start] == '0':
                path.append(s[start])
                _dfs(start+1, path)
                path.pop()
                return
            # 递归查找
            for i in range(start, len(s)):
                if 0 <= int(s[start:i+1]) <= 255:
                    path.append(s[start:i+1])
                    _dfs(i+1, path)
                    path.pop()
                else:
                    break
            return

        ans = []
        _dfs(0, [])
        return ans
```
