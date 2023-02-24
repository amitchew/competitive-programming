class ListNode:
    def __init__(self,val=0,prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next
        

class MyLinkedList:

    def __init__(self):
        self.len = 0
        self.head = ListNode()
        self.tail = ListNode(0,self.head,None)
        self.head.next = self.tail

	# determine the walking direction based on index
    def find_prev(self,index):
        if index <= self.len//2:
            cur = self.head
            for _ in range(index):
                cur = cur.next
        else:
            cur = self.tail.prev
            for _ in range(self.len-index):
                cur = cur.prev
        return cur
        
    
    def get(self, index: int) -> int:
        return self.find_prev(index).next.val if 0  <= index < self.len else -1
        

    def addAtHead(self, val: int) -> None:

        self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.len,val)
        

    def addAtIndex(self, index: int, val: int) -> None:

        if 0  <= index <= self.len:
            prev = self.find_prev(index)
            node = ListNode(val,prev,prev.next)
            prev.next.prev = node
            prev.next = node
            self.len += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if 0  <= index < self.len:
            cur = self.find_prev(index)
            cur.next.next.prev = cur
            cur.next = cur.next.next
            self.len -= 1
