# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。 
# 
#  
# 
#  示例 : 
# 给定二叉树 
# 
#            1
#          / \
#         2   3
#        / \     
#       4   5    
#  
# 
#  返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。 
# 
#  
# 
#  注意：两结点之间的路径长度是以它们之间边的数目表示。 
#  Related Topics 树 
#  👍 595 👎 0


# 543 - diameter-of-binary-tree

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.())