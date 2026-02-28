class Solution () :
    def minimumFlips(self, n : int) -> int:
        s = bin(n)[2: ]
        count = 0
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                count += 2
            l += 1
            r -= 1
        return count