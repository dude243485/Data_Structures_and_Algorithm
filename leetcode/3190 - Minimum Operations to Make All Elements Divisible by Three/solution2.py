from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = 0
        for i in nums:
            if i % 3 != 0:
                counter += 1
        return counter
    
nums = [4]
test = Solution()
print(test.minimumOperations(nums))