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
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        finds = [head.val, ]
        p = head
        while p.next:
            node = p.next
            if node.val in finds:
                p.next = p.next.next
            else:
                p = p.next
                finds.append(node.val)
        return head



if __name__ == '__main__':
    mm = Solution()
    head = ListNode(None)
    cur = head
    for i in [1, 2, 3, 3, 2, 1]:
        cur.next = ListNode(i)
        cur = cur.next
    head = head.next
    res = mm.removeDuplicateNodes(head)

    ### 打印结果
    while res:
        print(res.val, end=" ")
        res = res.next