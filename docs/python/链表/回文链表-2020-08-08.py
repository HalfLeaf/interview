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
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return True
        res = []
        while head :
            res.append(head.val)
            head = head.next
        i = 0
        j = len(res)-1
        while i<j:
            if res[i] == res[j]:
                i+=1
                j-=1
            else:
                return False
        return True




if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(None)
    cur = l1
    for i in [7,1,6]:
        cur.next = ListNode(i)
        cur = cur.next
    l1 = l1.next
    res = s.isPalindrome(l1)

    ### 打印结果
    while res:
        print(res.val, end=" ")
        res = res.next