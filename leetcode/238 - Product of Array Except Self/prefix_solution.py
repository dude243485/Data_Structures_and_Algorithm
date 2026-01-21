from typing import List


input = [1,2,3,4]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [1] * n
        
        prefix = 1
        for i in range(len(nums)):
            arr[i] = prefix
            prefix *= nums[i]
            
        for i in range(n-1, -1, -1):
            arr[i] *= suffix
            suffix *= nums[i]
            
        return arr
    
test = Solution()
answer = test.productExceptSelf(input)
print(answer)