# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def maxDepth(root):
            if not root:
                return 0

            return 1 + max(maxDepth(root.left), maxDepth(root.right))

        curr = maxDepth(root.left) + maxDepth(root.right)
        return max(curr, max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)))