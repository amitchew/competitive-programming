# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head = []
        if not head or not head.next:
            return head


        dummyHead=ListNode()
        dummy=dummyHead

        while head:
            next_node=head.next
            # head = [1]
            if not next_node:
                next_Head=None
                head=None
            ######  
            else:  
                next_Head=next_node.next
                dummy.next=next_node
                next_node.next=head

                head.next= next_Head 
                dummy=head
                head=next_Head 
        return dummyHead.next
