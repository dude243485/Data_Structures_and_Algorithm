from typing import List
"""Brute Force"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        ansStack = []
        n = len(temperatures)
        cMax = temperatures[0]
        for i in range(n):           
            pos = i
            while  pos < n - 1 and temperatures[i] > temperatures[pos + 1] :
                pos += 1
            ansStack.append(max(0, pos - i + 1))
        
        return ansStack
            
    


tokens = [73,74,75,71,69,72,76,73]
test = Solution()
print(test.dailyTemperatures(tokens))
print([1,1,4,2,1,1,0,0])