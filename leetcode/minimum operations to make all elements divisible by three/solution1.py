from typing import List
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        minOpp = 0
        for i in range(len(nums)):
            c_1 = c_2 = nums[i]
            count1 = count2 = 0
            
            while True:
                if c_1 % 3 == 0:
                    minOpp += count1
                    break
                elif c_2 % 3 == 0:
                    minOpp += count2
                    break
                #decrement and increment the numbers
                c_1 += 1
                c_2 -= 1
                
                #increment operations
                count1 += 1
                count2 += 1
                      
        return minOpp
            
        
        

nums = [1,2,3,4]
test = Solution()
print(test.minimumOperations(nums))