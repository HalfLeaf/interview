# 从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任
# 意数字。A 不能视为 14。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [1,2,3,4,5]
# 输出: True 
# 
#  
# 
#  示例 2: 
# 
#  输入: [0,0,1,2,5]
# 输出: True 
# 
#  
# 
#  限制： 
# 
#  数组长度为 5 
# 
#  数组的数取值为 [0, 13] . 
#  👍 90 👎 0


# 剑指 Offer 61 - bu-ke-pai-zhong-de-shun-zi-lcof

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.())