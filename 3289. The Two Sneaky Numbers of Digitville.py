class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                    if  nums[i] == nums[j]:
                        res.append(nums[i])
        return res
                