class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:  
        dummy_node = ListNode(0, head)
        
        leftPrev, curr = dummy_node, head
        for i in range(left - 1):
            leftPrev, curr = curr, curr.next 

        prev = None
        for i in range(right - left + 1):
            tnext = curr.next 
            curr.next = prev 
            prev, curr = curr, tnext 

        
        leftPrev.next.next = curr
        leftPrev.next = prev
        return dummy_node.next
