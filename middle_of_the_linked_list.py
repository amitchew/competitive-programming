class Solution:
    def middleNode(self, head: [ListNode]) -> [ListNode]:
        lower = head
        upper = head
        while upper and upper.next:
            lower = lower.next
            upper = upper.next.next
        return lower 
