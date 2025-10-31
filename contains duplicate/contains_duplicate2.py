from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        i = 1
        while i < len(nums):
            if (nums[i] == nums[i-1]):
                return True
            i += 1
        return False
    
nums = [1, 2, 2, 3]
test = Solution()
print(test.hasDuplicate(nums))