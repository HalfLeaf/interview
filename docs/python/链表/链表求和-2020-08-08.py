#-*-coding:utf-8-*-
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        pv = ""
        while p.next:
            pv = f"{pv}{p.val}"
            p = p.next
        pv = f"{pv}{p.val}"
        
        q = l2
        qv = ""
        while q.next:
            qv = f"{qv}{q.val}"
            q = q.next
        qv = f"{qv}{q.val}"
        result = str(int(pv[::-1]) + int(qv[::-1]))
        head = ListNode(int(result[0]))
        for i in result[1:]:
            node = ListNode(int(i))
            node.next = head
            head = node
        return head



if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(None)
    cur = l1
    for i in [7,1,6]:
        cur.next = ListNode(i)
        cur = cur.next
    l1 = l1.next
    l2 = ListNode(None)
    cur = l2
    for i in [5,9,2]:
        cur.next = ListNode(i)
        cur = cur.next
    l2 = l2.next
    res = s.addTwoNumbers(l1, l2)

    ### 打印结果
    while res:
        print(res.val, end=" ")
        res = res.next