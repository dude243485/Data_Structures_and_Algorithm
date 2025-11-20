from typing import List

#return an array such that the i-th element of the array is equal to the sum of all previous array elements
#this is a prefix sum problem

input = [1,2,3,4]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        num_of_zeros = 0
        for i in nums:
            if i != 0:
                product = product * i
                
            else:
                num_of_zeros += 1
            
        res_arr = []
        for i in nums:
            if i == 0 and num_of_zeros  < 2:
                res_arr.append(int(product))
                
            elif i != 0 and num_of_zeros >= 1:
                res_arr.append(0)
                
            elif i != 0 and num_of_zeros == 0:    
                res_arr.append(int(product/i))
        
        return res_arr
            
            

test = Solution()
answer = test.productExceptSelf(input)
print(answer)