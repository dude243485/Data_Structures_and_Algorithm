class Solution:
    def numberOfSteps(self, num: int) -> int:
        n = bin(num)[2:]
        ones = 0
        for i in n:
            if i == "1":
                ones += 1
        
        return ones + (len(n) - 1)
        