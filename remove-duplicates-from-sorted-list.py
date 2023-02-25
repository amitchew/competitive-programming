# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = head
        while x:
            while x.next and x.val == x.next.val:
                x.next = x.next.next
            x = x.next
        return head
