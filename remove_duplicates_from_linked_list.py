class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = head
        while x:
            while x.next and x.val == x.next.val:
                x.next = x.next.next
            x = x.next
        return head
