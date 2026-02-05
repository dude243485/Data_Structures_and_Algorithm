
from typing import List
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        prefix_arr = []
        n = len(nums)
        curr_sum = 0
        for i in range(n):
            curr_sum += nums[i]
            prefix_arr.append(curr_sum)
            
        total = 0
        
        for i in range(n):
            
            start = max(0, i - nums[i])
            if start == 0:
                this_sum = prefix_arr[i]
            else:
                this_sum = prefix_arr[i] - prefix_arr[start - 1]
            total += this_sum
        return total 
            
               
        
nums =[2, 3, 1]
test = Solution()
answer = test.subarraySum(nums)
print(answer)