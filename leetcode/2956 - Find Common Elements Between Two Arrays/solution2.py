class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1 = {}
        map2 = {}
        n1 = len(nums1)
        n2 = len(nums2)

        for i in range(n1):
            map1[nums1[i]] = map1.get(nums1[i], 0) + 1
        for j in range(n2):
            map2[nums2[j]] = map2.get(nums2[j], 0) + 1

        count1 = 0
        count2 = 0
        for n in map1.keys():
            if n in map2:
                count1 += map1[n]
        
        for n in map2.keys():
            if n in map1:
                count2 += map2[n]
        
        return [count1, count2]
        
        