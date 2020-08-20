#-*-coding:utf-8-*-

from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SingleLinkList:
    def __init__(self, node=None):
        self.__head = node

    def is_Empty(self):
        return self.__head is None

    def append(self, item): # 尾插法
        node = ListNode(item)
        if self.is_Empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def find_head(self):
        return self.__head


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


if __name__ == '__main__':
    mm = Solution()
    head = ListNode(None)
    cur = head
    for i in [1, 2, 3, 3, 2, 1]:
        cur.next = ListNode(i)
        cur = cur.next
    head = head.next
    print(mm.kthToLast(head, 2))