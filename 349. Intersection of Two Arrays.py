class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen1 = set()
        arr =[]
        for i in range(len(nums1)):
            seen1.add(nums1[i])
        
        for j in range(len(nums2)):
            if nums2[j] in seen1 :
                arr.append(nums2[j])
                seen1.remove(nums2[j])
        return arr