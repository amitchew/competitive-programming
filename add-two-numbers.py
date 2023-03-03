# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        remaind = 0
        current = dummyHead
        
        while l1 or l2:
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0
            
            sum_ = l1_val + l2_val + remaind
            
            current.next = ListNode(sum_ % 10)
            current = current.next
            remaind = sum_ // 10
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if remaind:
            current.next = ListNode(remaind)
        
        return dummyHead.next
