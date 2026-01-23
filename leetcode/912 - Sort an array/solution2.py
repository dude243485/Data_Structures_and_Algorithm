
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(leftArr, rightArr, arr):
            leftSize = len(arr)//2
            rightSize = len(arr) - leftSize
            i = 0
            l = 0
            r = 0
            
            while ( l < leftSize and r < rightSize):
                if leftArr[l] < rightArr[r]:
                    arr[i] = leftArr[l]
                    i += 1
                    l += 1
                else:
                    arr[i] = rightArr[r]
                    i += 1
                    r += 1
            while (l < leftSize):
                arr[i] = leftArr[l]
                i += 1
                l += 1
            while (r < rightSize):
                arr[i] = rightArr[r]
                i += 1
                r += 1
                    
            
        def mergeSort(arr) :
            n = len(arr)
            if n <= 1: return #base case
            
            
            leftArr , rightArr = [], []
            middle = n//2
             
            for l in range(n):
                if (l < middle): leftArr.append(arr[l])
                else:  rightArr.append(arr[l])
            mergeSort(leftArr)
            mergeSort(rightArr)
            merge(leftArr, rightArr, arr)
        
        mergeSort(nums)
        return nums
                   

            
nums = [5,1,1,2,0,0]
test = Solution()
print(test.sortArray(nums))