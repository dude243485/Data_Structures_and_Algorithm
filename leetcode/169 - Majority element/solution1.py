from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        threshold = int(n/2)
        map = {}
        
        for i in range(n):
            map[nums[i]] = map.get(nums[i], 0) + 1
            if map[nums[i]] > threshold: return nums[i]

nums = [2,2,1,1,1,2,2]
test = Solution()
print(test.majorityElement(nums))