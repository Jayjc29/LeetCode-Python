# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        count = 0
        current = head 
        while current != None:
            count = count * 2 + current.val
            current = current.next 
        return count
        