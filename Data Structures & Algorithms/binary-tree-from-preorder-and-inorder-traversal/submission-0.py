# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) <= 0 or len(inorder) <= 0:
            return None
        
        rootNode = TreeNode(preorder[0])

        mid = inorder.index(rootNode.val)

        left_inorder = inorder[:mid]
        right_inorder = inorder[mid+1:]

        left_preorder = preorder[1:len(left_inorder)+1]
        right_preorder = preorder[len(left_inorder) + 1 :]

        rootNode.left = self.buildTree(left_preorder, left_inorder)
        rootNode.right = self.buildTree(right_preorder, right_inorder)

        return rootNode