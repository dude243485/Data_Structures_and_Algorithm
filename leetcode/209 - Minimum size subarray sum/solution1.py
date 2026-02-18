from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        arrSum = 0
        i = 0
        minW = float("inf")

        for r in range(n):
            arrSum += nums[r]
            while arrSum >= target:
                minW = min(minW, r - i + 1)
                arrSum -= nums[i]
                i += 1

        if minW == float("inf"): return 0
            
        return minW
        