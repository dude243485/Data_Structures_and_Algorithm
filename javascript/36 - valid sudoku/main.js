/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {

    let hashMap = new Map();
    let m = board.length;
    let n = board[0].length;

    for (let row =0 ; row < m ; row++ ){
        for (let col = 0; col < n; col ++){
            let cell = board[row][col]
            if(cell === "."){
                continue;
            }

            if (hashMap.has(cell)){
                let rowList = [...hashMap.get(cell)[0]];
                let colList = [...hashMap.get(cell)[1]];

                for (let i = 0 ; i < rowList.length; i ++){
                    if(Math.floor(row / 3) === Math.floor(rowList[i] /3 ) && Math.floor(col /3) === Math.floor(colList[i]/3)){
                        return false;
                    }
                }

                if (hashMap.get(cell)[0].includes(row) || hashMap.get(cell)[1].includes(col)){
                    return false;
                } else {
                    hashMap.get(cell)[0].push(row);
                    hashMap.get(cell)[1].push(col);
                }

            } else {
                hashMap.set(cell, [[row], [col]]);
            }
        }
    }
    return true;
    
};