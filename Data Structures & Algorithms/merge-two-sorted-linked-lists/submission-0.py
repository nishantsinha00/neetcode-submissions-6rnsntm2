# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = list1, list2
        newHead = None

        if not head1:
            return head2

        if not head2:
            return head1
        if head1.val > head2.val:
            newHead = head2
            head2 = head2.next
        else:
            newHead = head1
            head1 = head1.next

        temp = newHead
        
        while head1 and head2:
            if head1.val > head2.val:
                temp.next = head2
                head2 = head2.next
            else:
                temp.next = head1
                head1 = head1.next

            temp = temp.next

        if head1:
            temp.next = head1

        if head2:
            temp.next = head2

        return newHead

        