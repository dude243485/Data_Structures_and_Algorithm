from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        left = 0
        length = len(nums)
        for right in range(k-1, length):
            current = nums[left:right+1]
            res.append(max(current))
            left += 1
        return res
            
        
    

nums = [1,3,-1,-3,5,3,6,7]
k = 3
test = Solution()
print(test.maxSlidingWindow(nums, k))