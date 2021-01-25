# 给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。 
# 
#  
# 
#  示例: 
# 
#  输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 
# 输出:  [1,2,4,7,5,3,6,8,9]
# 
# 解释:
# 
#  
# 
#  
# 
#  说明: 
# 
#  
#  给定矩阵中的元素总数不会超过 100000 。 
#  
#  👍 164 👎 0


# 498 - diagonal-traverse

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.())