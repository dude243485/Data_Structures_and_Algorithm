from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        hashSet = set(nums)

        if 1 not in hashSet:
            return 1
        
        for i in range(len(nums)):
            if nums[i] > 0 and nums[i] + 1 not in hashSet:
                return nums[i] + 1
    

nums = [1,2,0]
test = Solution()
answer = test.firstMissingPositive(nums)
print(answer)