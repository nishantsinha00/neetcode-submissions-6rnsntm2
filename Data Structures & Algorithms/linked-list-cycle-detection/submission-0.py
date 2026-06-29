# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i = 0
        while head and i <= 1000:
            head = head.next
            i += 1

        if i > 1000:
            return True

        return False