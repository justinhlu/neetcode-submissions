# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node, maxf):
            nonlocal res
            if node is None:
                return 0
            
            leftMax = dfs(node.left, maxf)
            rightMax = dfs(node.right, maxf)
            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)

            maxf = max(leftMax, rightMax)
            res = max(res, node.val + leftMax + rightMax)
            return maxf + node.val

        dfs(root, 0)
        return res
