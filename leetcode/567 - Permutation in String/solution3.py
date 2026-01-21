class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len (s1)    
        n2 = len(s2)
        if n1 > n2:
            return False
        
        s1_dict = {}
        s2_dict = {}
        for i in range(ord('a') , ord('z') + 1):
            s1_dict[chr(i)] = 0
            s2_dict[chr(i)] = 0
            
        
        for i in range(n1):
            s1_dict[s1[i]] += 1
            s2_dict[s2[i]] += 1
            
        if s1_dict == s2_dict:
            return True
        
        for i in range(n1, n2):
            s2_dict[s2[i]] += 1
            s2_dict[s2[i-n1]] -= 1
            if s1_dict == s2_dict:
                return True
        return False
        
            
        
s1 = "adc"
s2 = "dcda"     
test = Solution()
print(test.checkInclusion(s1, s2))