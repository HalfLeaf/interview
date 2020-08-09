# 快慢指针类型

## 经典题库

:::tip 题目
判断链表中是否有环
:::

### 解题思路

我们可以使用两个指针而不是一个指针

第一个指针从列表的开头向前移动 n+1 步，而第二个指针将从列表的开头出发

现在，这两个指针被 n 个结点分开

我们通过同时移动两个指针向前来保持这个恒定的间隔，直到第一个指针到达最后一个结点

此时第二个指针将指向从最后一个结点数起的第 n 个结点

我们重新链接第二个指针所引用的结点的 next 指针指向该结点的下下个结点


```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        '''
        利用列表寻找是否存在重复的对象，时间复杂度O（n）,空间复杂度O（n）
        if not head:
            return head
        m = []
        while head:
            if head in m:
                return True
            m.append(head)
            head = head.next
        return False
        '''
        # 快慢双指针追赶碰撞解法，时间复杂度为O（n）,空间复杂度为O（1）
        if not head:
            return head
        slow = head
        quick = head
        while quick and slow:
            # 这里因为quick是跳两次，所以要判断quick和quick.next是否都为空，否则会报NoneType的异常
            slow = slow.next
            if quick.next:
                quick = quick.next.next
            else:
                return False
            if quick is slow:
                return True
        return False
```