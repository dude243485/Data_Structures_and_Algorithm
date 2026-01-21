from typing import List

"""This solution uses the 2 pointer approach, 
it puts one pointer at the begining and 
another pointer at the end. at every iteration, 
if the sum is greater than the target, reduce the right pointer
if the sum is less than the target, increase the left pointer. 
Else return your solution.

This approach works because the array is already sorted."""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1
        while True:
            if (numbers[left] + numbers[right] > target):
                right -= 1
            elif (numbers[left] + numbers[right] < target):
                left += 1
            else:
                return [left + 1, right + 1]
        
    
input_data = ([2,3,4], 6)        
test = Solution()
print(test.twoSum(*input_data))