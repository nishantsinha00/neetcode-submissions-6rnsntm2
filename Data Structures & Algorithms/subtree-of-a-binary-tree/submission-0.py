# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False
        if not root:
            return res

        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            
            if (not p) and (not q):
                return True

            if (not p) or (not q):
                return False

            if p.val == q.val:
                return True and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            
            return False

        if isSameTree(root, subRoot):
            res = True

        else:
            res = self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        return res
        

