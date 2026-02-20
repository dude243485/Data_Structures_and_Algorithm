class Solution:
    def mirrorDistance(self, n: int) -> int:
        m = str(n)
        t = ""
        for i in range(len(m) - 1, -1, -1): 
            t += m[i]
            
        return abs(n - int(t))