from typing import List
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        count = 0
        for i in range(0, n-2 ):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    a = nums[j] - nums[i]
                    b = nums[k] - nums[j]
                    if a == diff and b== diff:
                        print([nums[i], nums[j], nums[k]])
                        count += 1

        return count
        