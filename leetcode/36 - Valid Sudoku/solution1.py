from typing import List
class Solution:
    def isValidSudoku(self, board: List[list[str]]) -> bool:
        map = {}
        for i in range(1, 10):
            map[str(i)] = []
        
        
        
        rows, cols = len(board), len(board[0])
        for r in range(rows):
            for c in range(cols):
                if board[r][c] != "." and map[board[r][c]] == []:
                    print("first inputs")
                    map[board[r][c]].append([r, c])
                elif board[r][c] != "." and len(map[board[r][c]]) > 0:
                    #check rows and columns
                    for i in map[board[r][c]]:
                        if r == i[0] or c == i[1]:
                            
                            return False
                        
                    #check for 3x3 boxes
                    for i in map[board[r][c]]:
                        if r // 3 == i[0] // 3 and c // 3 == i[1] // 3:
                            return False   
                    map[board[r][c]].append([r, c])
                   
        return True
                    
                
        
          
       
    

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
test = Solution()
answer = test.isValidSudoku(board)
print(answer)