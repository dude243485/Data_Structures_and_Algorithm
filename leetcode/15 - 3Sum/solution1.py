from typing import List

"""Brute force approach"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer =[]
        for i in range(0, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (nums[i] + nums[j] + nums[k]) == 0:
                        answer.append([nums[i], nums[j], nums[k]])
                        
        return answer
            
    

input = [-1,0,1,2,-1,-4]
test = Solution()
print(test.threeSum(input))