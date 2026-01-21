from typing import List

"""Solution was based on the sliding window approach"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        l = 0
        r = 1
        res = 0
        
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r += 1
            
            else:
                res = max(res, prices[r] - prices[l])
                r += 1
        return res
            

    
input_data = [7,1,5,3,6,4]      
test = Solution()
print(test.maxProfit(input_data))