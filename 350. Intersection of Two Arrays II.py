from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)
        arr = []

        for num in nums2 :
            if count[num] > 0 :
                arr.append(num)
                count[num] -= 1

        return arr