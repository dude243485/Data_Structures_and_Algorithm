
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition (arr, p, r):
            pivot = arr[r]
            index = p - 1
            for j in range(p, r):
                if arr[j] <= pivot:
                    index += 1
                    arr[j], arr[index] = arr[index], arr[j]
            
            arr[r] = arr[index+1]
            arr[index + 1] = pivot
            return index + 1
        
        def quickSort( arr, p, r):
            if p < r:
                q = partition(arr, p, r)
                quickSort(arr, p, q-1)
                quickSort(arr, q+1, r)
        
        n = len(nums)
        quickSort(nums, 0, n-1)
        return nums

nums = [5,2,3,1]
test = Solution()
print(test.sortArray(nums))