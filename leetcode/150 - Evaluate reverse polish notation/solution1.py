from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-/*"
                
        stack =  []
        n = len(tokens)
        p = 0
        
        while p < n:
            if tokens[p] not in operators:
                stack.append(tokens[p])
                
            else:
                opp = tokens[p]
                last = int(stack.pop())
                
                if opp == "+":
                    stack[-1] = int(stack[-1]) + last
                elif opp == "-":
                    stack[-1] = int(stack[-1]) - last
                elif opp == "*":
                    stack[-1] = int(stack[-1]) * last
                else:
                    stack[-1] = int(int(stack[-1]) /  last)
                    
            p += 1
            
        return int(stack[-1])        
        
        
    
    
tokens = ["2","1","+","3","*"]
test = Solution()
print(test.evalRPN(tokens))