class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = left +1

        while right < len(nums):
            if nums[left] == nums[right]:
                return nums[left]
                break
            else :
                left  +=1
                right +=1

