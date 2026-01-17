from typing import List
"""Brute Force"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        posStack = []
        n = len(temperatures)
        ans = [0] * n
        
        for i in range(n):
            next = temperatures[i]
            
            while stack and  next > stack[-1]:
                pos = posStack[-1]
                wait = i - pos
                ans[pos] = wait
                stack.pop()
                posStack.pop()
                
            stack.append(next)
            posStack.append(i)
        
        return ans
        
        
tokens = [73,74,75,71,69,72,76,73]
test = Solution()
print(test.dailyTemperatures(tokens))
print([1,1,4,2,1,1,0,0])