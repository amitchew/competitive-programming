# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        head = [4,2,1,3]
        dummy=0
        0-4-2-1-3
        dummy.next.val <= dummy.next.next.val

        '''
        dummyNode=ListNode(0)
        dummyNode.next=head
        temp=dummyNode
        
        while(temp.next and temp.next.next):
            if temp.next.val<=temp.next.next.val:
                temp=temp.next
                
            else:
                current=temp.next.next
                temp.next.next=current.next

                other_temp=dummyNode

                while other_temp.next.val<=current.val:
                    other_temp=other_temp.next

                current.next=other_temp.next
                other_temp.next=current

        return dummyNode.next
