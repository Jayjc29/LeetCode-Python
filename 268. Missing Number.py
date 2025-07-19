class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = 0 
        total = 0 
        for i in range(len(nums)):
            length += 1
            total = total + nums[i]
        
        total_sum  = length *(length+1)//2

        res = total_sum - total 
        return res 
