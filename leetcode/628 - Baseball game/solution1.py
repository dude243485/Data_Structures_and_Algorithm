
from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        tokens = "D+C"
        stack = []
        
        n = len(operations)
        for i in range(n):
            if operations[i] not in tokens:
                stack.append(int(operations[i]))
            
            else:
                if operations[i] == "+":
                    stack.append(stack[-1] + stack[-2])
                
                elif operations[i] == "D":
                    stack.append(stack[-1] * 2) 
                
                elif operations[i] == "C":
                    stack.pop()
                    
        return sum(stack)
        
        
operations = ["5","2","C","D","+"]
test = Solution()
print(test.calPoints(operations))