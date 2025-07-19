class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        arr = []
        for i in range(len(nums)):
            seen.add(nums[i])
        for i in range(1,len(nums)+1):
            if i not in seen :
                arr.append(i)
            else:
                continue
        return arr