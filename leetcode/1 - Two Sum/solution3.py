from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        n = len(nums)
        
        for i in range(n):
            key = target - nums[i]
            if key in map:
                return [map[key], i]
            map[nums[i]] = i
        return 
        


    
nums = [2,7,11,15]
target = 9
test = Solution()
answer = test.twoSum(nums, target)
print(answer)