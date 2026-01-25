from typing import List

class Solution:
    def isValidSudoku(self, board: List[list[str]]) -> bool:
        map = {}
        for i in range(9):
            map[i+"r"] = []
            map[i +"c"] = []
        
        print(map)
        
        rows, cols = len(board), len(board[0])
        
        for r in range(rows):
            
            for c in range(cols):
                if board[r][c].isalpha() and (r in map[r+"r"] or c in map[c+"c"]):
                    return False
                elif not board[r][c].isalpha():
                    continue
                
                else:
                    map[i+"r"].append(r)
                    map[i +"c"].append(c)
        return True
                    

                    
                
                
        