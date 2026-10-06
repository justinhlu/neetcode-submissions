# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, maxf):
            nonlocal res
            if node is None:
                return
            
            if node.val >= maxf:
                res += 1

            currMax = max(maxf, node.val)
            dfs(node.left, currMax)
            dfs(node.right, currMax)
        
            return 
        
        dfs(root, float('-inf'))

        return res
