from typing import List
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        cols = len(image[0])
        for row in image:
            l = 0
            r = cols - 1
            while l <= r:
                row[l], row[r] = (row[r] + 1) % 2, (row[l] + 1) % 2
                r = r - 1
                l = l + 1
                
        return image
    
image = [[1,1,0],[1,0,1],[0,0,0]]
test = Solution()
answer = test.flipAndInvertImage(image)
print(answer)