
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)   
        n = len(nums)
        sample = nums[:]
        target = n - k

        for i in range(0, k):
            nums[i] = sample[target+i]
        
        for j in range(k, n):
            nums[j] = sample[j - k]


        