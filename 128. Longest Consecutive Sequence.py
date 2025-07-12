class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums :
            return 0
        nums .sort()
        arr= []
        count = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue 
            elif nums[i]+1 == nums[i+1]:
                count +=1 
            else :
                arr.append(count)
                count = 1
        arr.append(count)
        return max(arr)