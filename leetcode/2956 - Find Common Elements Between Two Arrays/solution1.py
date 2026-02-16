
from typing import List
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        first_set = set(nums1)
        second_set = set(nums2)

        count1, count2 = 0, 0
        n = max(len(nums1), len(nums2))

        for i in range(n):
            if i < len(nums1) and nums1[i] in second_set:
                count1 += 1
            if i < len(nums2) and nums2[i] in first_set:
                count2 += 1
        
        return [count1, count2]