from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_max = 0
        curr_sum = 0
        for n in gain:
            curr_sum += n
            curr_max = max(curr_max, curr_sum)
        return curr_max