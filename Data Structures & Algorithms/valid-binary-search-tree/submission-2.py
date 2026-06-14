# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        INF = 2000
        q = deque()
        q.append((root, -INF, INF))

        while q:
            for _ in range(len(q)):
                curr, left, right = q.popleft()
                if not curr:
                    continue
                if not left < curr.val < right:
                    return False
                q.append((curr.left, left, curr.val)) 
                q.append((curr.right, curr.val,right))

        return True



