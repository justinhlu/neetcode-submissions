# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        sameTree = True

        def dfs(node1, node2):
            nonlocal sameTree
            if node1 is None:
                if node2:
                    sameTree = False
            if node2 is None:
                if node1:
                    sameTree = False

            if node1 and node2:
                nodeLeft = dfs(node1.left, node2.left)
                nodeRight = dfs(node1.right, node2.right)

                if node1.val != node2.val:
                    sameTree = False

            return 0
        
        dfs(p,q)

        return sameTree
