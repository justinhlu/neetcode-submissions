# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    maxDiameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxDiameter = 0

        def dfs(root):
            nonlocal maxDiameter

            if root:
                leftHeight = dfs(root.left)
                rightHeight = dfs(root.right)
                d = leftHeight + rightHeight
                if d > maxDiameter:
                    maxDiameter = d
                if leftHeight > rightHeight:
                    return 1 + leftHeight
                else:
                    return 1 + rightHeight
            return 0

        dfs(root)
        return maxDiameter
