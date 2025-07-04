class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for i in nums :
            if i%3 != 0 and (i %2 == 0 or i % 2 == 1) :
                res = res + 1
        return res