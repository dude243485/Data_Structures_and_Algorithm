from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashSet = set()
        w_length = k + 1

        for i in range(k+ 1):
            if i >= len(nums):
                return False
            if nums[i] in hashSet:
                return True
            hashSet.add(nums[i])
        
        l = 0
        for r in range(k+1, len(nums)):
            hashSet.remove(nums[l])
            if nums[r] in hashSet:
                return True
            hashSet.add(nums[r])
            l += 1
        
        return False


          