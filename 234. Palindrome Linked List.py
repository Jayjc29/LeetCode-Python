class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr  = head
        arr = []

        while curr != None:
            arr .append(curr.val)
            curr = curr.next 


        left = 0
        right = len(arr)-1

        while left < right :
            if arr[left] == arr[right]:
                left = left+1 
                right = right -1
            else :
                return False
        return True