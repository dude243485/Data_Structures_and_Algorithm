from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[int(len(nums)/2) + 1]

nums = [2,2,1,1,1,2,2]
test = Solution()
print(test.majorityElement(nums))