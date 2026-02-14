class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        total = 0
        n = len(s)

        for i in range(n):
            char = s[i]
            total += abs(i - t.index(char))
        return total