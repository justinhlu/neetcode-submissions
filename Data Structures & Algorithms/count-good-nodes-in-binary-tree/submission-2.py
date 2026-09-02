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

            if node:
                if node.val >= maxSoFar:
                    res += 1
                    maxSoFar = max(maxSoFar, node.val)
                
                if node.left:
                    dfs(node.left, maxSoFar)
                if node.right:
                    dfs(node.right, maxSoFar)
            
            return 0

        
        dfs(root, root.val)
        return res