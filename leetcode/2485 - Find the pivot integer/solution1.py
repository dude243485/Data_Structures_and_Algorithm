class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1: return 1 #edge case
        if n < 5: return -1 #edge cases
        prefix = [0] * n
        sum = 0
        for i in range(1, n+1):
            sum += i
            prefix[i-1] = sum
        
        for i in range(n):
            if prefix[i] == prefix[-1] - prefix[i-1]:
                return i+1
        return -1

