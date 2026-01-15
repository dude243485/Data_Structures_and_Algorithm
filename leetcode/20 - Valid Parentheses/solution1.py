class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        open, close = "({[", ")}]"
        stack = []
        for i in range(len(s)):
            if s[i] in open:
                stack.append(s[i])

            #check if a closing is coming before an opening
            elif s[i] not in open and not stack: return False
            
            else:
                if close.index(s[i]) ==  open.index(stack[-1]):
                    stack.pop()
                else:
                    return False
                
        #check if stack is empty        
        if stack: return False
        return True
            
    
    
s = "()"
test = Solution()
print(test.isValid(s))