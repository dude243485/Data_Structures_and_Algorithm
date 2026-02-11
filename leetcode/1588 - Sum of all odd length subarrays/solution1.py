

from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix = [0]*len(arr)
        sum= 0
        for i in range(len(arr)):
            sum += arr[i]
            prefix[i] = sum

        total = prefix[-1]
        n = len(arr)
        for j in range(2, n, 2):
            i = 0
            k = i + j
            while k < n:
                if i == 0:
                    total += prefix[k]
                    i += 1
                    k += 1
                    continue
                
                total += prefix[k] - prefix[i-1]
                i += 1
                k += 1
        return total

        