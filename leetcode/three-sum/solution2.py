from typing import List

"""Brute force approach"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort() #first sort the array
        answer = set()
        for i in range(0, len(nums) - 2):
            if i>0 and nums[i-1]==nums[i]:
                continue

            left = i + 1
            right = len(nums) - 1
            
            while (left < right):
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    answer.add(tuple([nums[i], nums[left], nums[right]]))
                    left += 1
                    right -= 1
                    while nums[left] == nums[left -1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                    
                elif sum < 0:
                    left += 1
                    
                elif sum > 0:
                    right -= 1
        return list(answer)
        
                    

input = [-1,0,1,2,-1,-4]
test = Solution()
print(test.threeSum(input))