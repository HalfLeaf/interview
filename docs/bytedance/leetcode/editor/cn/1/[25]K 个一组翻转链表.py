# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。 
# 
#  k 是一个正整数，它的值小于或等于链表的长度。 
# 
#  如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。 
# 
#  
# 
#  示例： 
# 
#  给你这个链表：1->2->3->4->5 
# 
#  当 k = 2 时，应当返回: 2->1->4->3->5 
# 
#  当 k = 3 时，应当返回: 3->2->1->4->5 
# 
#  
# 
#  说明： 
# 
#  
#  你的算法只能使用常数的额外空间。 
#  你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。 
#  
#  Related Topics 链表 
#  👍 863 👎 0


# 25 - reverse-nodes-in-k-group

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.())