# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head :
            return head
        
        length = 1
        tail = head
        while tail.next != 0 :
            tail = tail.next 
            length = length+1


        k = k % length

        if k == 0 :
            return head
        

        curr = head

        for i in range (length - k - 1):
            curr = curr.next 
        new_node = curr.next 
        curr.next = None
        tail.next = head 
        return 