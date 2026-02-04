from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        p2 = 0
        nums3 = nums1[:m]
        i = 0
        while p1 < m and p2 < n:
            if nums2[p2] < nums3[p1]:
                nums1[i] = nums2[p2]
                p2 = p2 + 1
                i = i + 1
            
            else:
                nums1[i] = nums3[p1]
                p1 = p1 + 1
                i = i + 1
        
        for j in range(p1, m):
            nums1[i] = nums3[p1]
            p1 = p1 + 1
            i = i + 1
        
        for j in range(p2, n):
            nums1[i] = nums2[p2]
            p2 = p2 + 1
            i = i + 1      
                    
        return
    
nums1, m, nums2, n = [1, 2, 3 ,0, 0, 0], 3, [2, 5, 6], 3
test = Solution()
test.merge(nums1, m, nums2, n)
print(nums1)
                
            