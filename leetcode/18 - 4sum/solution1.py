
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() #first sort the array
        ans = set()
        for a in range(0, len(nums) - 3):
            # target1 = target - nums[a]
            subAns = set()
            for b in range(a+1, len(nums) - 2):
                if b > 0 and nums[b-1] == nums[b]:
                    continue
                
                left = b + 1
                right = len(nums) - 1

                while (left < right):
                    sum = nums[a] + nums[b] + nums[left] + nums[right]
                    if sum == target:
                        ans.add((nums[a], nums[b], nums[left], nums[right]))
                        left += 1
                        right -= 1
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1
                        while nums[right] == nums[right + 1] and left < right:
                            right -= 1
                    elif sum < target:
                        left += 1
                    elif sum > target:
                        right -= 1
        return list(ans)
                        
            
          
nums = [1,0,-1,0,-2,2]
target = 0
test = Solution()
print(test.fourSum(nums, target))
            