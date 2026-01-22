class Solution:
    def reverseDegree(self, s: str) -> int:
        n = len(s)
        sum = 0
        for i in range(n):
            order = ord(s[i]) - 96
            pos = (26 - order + 1)
            sum += pos * (i+1)
        return sum
            
    
s = "abc"
test = Solution()
print(test.reverseDegree(s))
print(27%(-1))
        