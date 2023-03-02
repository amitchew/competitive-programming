# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        now_at=head
        length=1
        while now_at.next:
            length+=1
            now_at=now_at.next
        now_at.next=head
        k=k%length

        k=length-k
        while k:
            now_at=now_at.next
            k-=1
        
        head=now_at.next
        now_at.next=None
        return head
