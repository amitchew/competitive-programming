# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        startt = dummy
        current = head
        while current:
            unique_flag = True
            while current.next and current.next.val == current.val:
                unique_flag = False
                current = current.next
            
            if unique_flag:
                startt.next = current
                startt = startt.next
            current = current.next
        startt.next = None
        return dummy.next
