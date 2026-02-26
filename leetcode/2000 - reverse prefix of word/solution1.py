class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        found = False
        
        for c in word:
            if c != ch:
                stack.append(c)
            else:
                stack.append(ch)
                found = True
                break
        n = len(stack)
        if not found : return word
        
        newStr = ""
        for i in range(len(stack)):
            newStr += stack.pop()
        print(newStr + word[n : ])
        return newStr + word[n : ]
        