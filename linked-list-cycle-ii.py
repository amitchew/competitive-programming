# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_set=set()
        now_at= head

        while now_at:
            if now_at in temp_set:
                return now_at

            else:
                temp_set.add(now_at)
                now_at=now_at.next
        return None

        
