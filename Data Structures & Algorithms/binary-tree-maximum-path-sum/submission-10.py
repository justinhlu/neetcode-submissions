# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node):
            nonlocal res
            if node is None:
                return 0
            
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)

            maxf = max(leftMax, rightMax)
            res = max(res, leftMax + rightMax + node.val)
            return node.val + maxf

        dfs(root)
        return res
