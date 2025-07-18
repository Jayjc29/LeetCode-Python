class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i >0 and nums[i] == nums[i-1]:
                continue 


            l,r = i+1,lens(nums)

            while l < r :
                s = nums[i] + nums[l] + nums[r]
                if s < 0 :
                    l= l+1
                elif s>0 :
                    r=r+1
                else :
                    res.append([nums[i],nums[l],nums[r]])
                    l +=1
                    r +=1
                
                while l < r and nums[l] == nums[l-1]:
                    l = l+1
                
                while l < r and nums[r] == nums [r+1]:
                    r = r-1
            return res