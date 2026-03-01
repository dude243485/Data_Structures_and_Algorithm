from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        n = len(nums)
        nums.sort()
        l , r = 0, n-1
        minElement = float("inf")
        while l < r:
            minElement = min (minElement, (nums[l] + nums[r])/2)
            l += 1
            r -= 1
            
        return minElement
        