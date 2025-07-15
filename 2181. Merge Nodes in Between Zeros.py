class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        forward = head 
        sum = 0
        
        while curr != None:
            if curr.val != 0:
                sum = sum + curr.val
            else :
                forward.next =ListNode(sum)
                forward = forward.next
                sum = 0 
            curr = curr.next 
        forward.next = None 
        return head.next 