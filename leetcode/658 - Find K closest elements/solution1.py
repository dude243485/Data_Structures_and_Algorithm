

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo, hi = 0, len(arr) - 1

        while hi - lo + 1 > k:
            left_dist = abs(arr[lo] - x)
            right_dist = abs(arr[hi] - x)

            if left_dist > right_dist:
                lo += 1
            else:
                hi -= 1

        return arr[lo : hi + 1]