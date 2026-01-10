class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        left = 0
        s1 = "".join(sorted(s1))
        for right in range(left+length-1, len(s2)):
            current = "".join(sorted(s2[left:right+1]))
            if (current == s1):
                return True
            left += 1
        return False
            
     
s1 = "ab"
s2 = "eidbaooo"     
test = Solution()
print(test.checkInclusion(s1, s2))