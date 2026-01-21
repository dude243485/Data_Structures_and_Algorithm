from typing import List
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        output = set()
        sample = ",".join(words)
        sample2 = "".join(words)
        lookUp = []
        r = 0
        for i in range(len(sample)):
            if sample[i] == ",":
                r += 1
                continue
            lookUp.append(r)
        print(sample2)
        print(lookUp)
            
        for i in range(len(sample2)):
            if sample2[i] == x:
                output.add(lookUp[i])
                
        return list(output)
        
        
        
        
        
    

words = ["leet","code"] 
x = "e" 
test = Solution()
print(test.findWordsContaining(words, x))