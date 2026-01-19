class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        init_str = []
        init_count = []
        str, count = "", 0
        for i in range(len(s)):
            if stack and  s[i] == "]":   
                while stack[-1].isalpha():
                    init_str.insert(0, stack.pop())
                    
                str = "".join(init_str)
                stack.pop() #remove the "["
                while stack and not stack[-1].isalpha() and not stack[-1] == "[":
                    init_count.insert(0, stack.pop())
                    
                count = int("".join(init_count))
                str = (str * count)
                stack.append(str)
                 
                #clean up
                str, count = "", 0
                
                init_str = []
                init_count = [] 
                continue
                
            stack.append(s[i])
            
        return "".join(stack)
    
s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
test = Solution()
print(test.decodeString(s))
