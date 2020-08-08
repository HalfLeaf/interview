#  返回倒数第k个节点

##  算法题

::: tip 题目

实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。

:::

~~~
示例1:
输入： 1->2->3->4->5 和 k = 2
输出： 4
~~~


说明：

给定的 k 保证是有效的


来源：&emsp; [力扣LeetCode](https://leetcode-cn.com/problems/kth-node-from-end-of-list-lcci/)


##  解答过程

### 我的思路

暴力美学:

遍历链表，获取节点总数，然后正序获取指定的节点


```python
#-*-coding:utf-8-*-
class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        cur = head
        count = 0
        # 指针指向None 表示到达尾部
        while cur is not None:
            count += 1
            # 指针下移
            cur = cur.next
        index = count - k
        i = 0
        p = head
        while i < index:
            p = p.next
            i += 1
        return p.val
```

* 耗时 32 ms
* 内存 13.6 MB
* 时间复杂度 O(N)
* 空间复杂度 O(1)

::: warning python源码文件位于
/python/链表/返回倒数第k个节点-2020-08-08.py
:::



##  大佬解法

::: tip 解法1
双指针

双指针同步移动法，即前指针先向前移动k个，然后双指针同步移动，当前指针移动到null时，后指针即指向倒数第k个

:::

```python
class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        target_node = head                      # 慢指针
        fast_node = head                        # 快指针
        steps = 0                               # 记录快指针的步数
        while fast_node:                        # 到尾结点时退出循环
            fast_node = fast_node.next          # 快指针移动一步
            if steps>=k:                        # 慢指针开始移动条件判断
                target_node = target_node.next  # 慢指针移动一步
            steps += 1                          # 累加步数
        return target_node.val                  # 返回目标节点的值
```

```python
class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        strt = head
        for i in range(k):
            head = head.next
        while head != None:
            strt = strt.next
            head = head.next
        return strt.val
```

::: tip 解法2
列表法：单次遍历-存储-取值；
:::

链表 => 列表 => 取值


```python
class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[-k]
```