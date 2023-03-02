# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp_list = []    
        while head:
            temp_list.append(head.val)
            head = head.next
                 
        leng = (len(temp_list)-1) // 2
             
        max_len = leng + 1
           
        summ = 0
        
        while leng > -1:
                                       
            if temp_list[leng] + temp_list[max_len] > summ:
                summ = temp_list[leng] + temp_list[max_len]
            
            leng -= 1
            max_len += 1
        return summ
        
            
            
        
        
