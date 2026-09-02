# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        
        def dfs(node, maxSoFar):
            nonlocal res
            if node is None:
                return
            
            if node.val >= maxSoFar:
                res += 1
                maxSoFar = max(node.val, maxSoFar)
            
            dfs(node.left, maxSoFar)
            dfs(node.right, maxSoFar)
        
        dfs(root, root.val)
        return res
            
