class Solution:
    def isSafe(self, board, i, j, num):
        for k in range(9):
            if(board[i][k] == num or board[k][j] == num):
                return False
            if(board[3 * (i // 3) + k // 3][3 * (j // 3) + k % 3] == num):
                return False
        return True
            
        
    def solveRecursive(self, board, i = 0):
        for i in range(i,9):
            for j in range(9):
                if(board[i][j] == "."):
                    numPossible = False
                    for k in range(1,10):
                        if(self.isSafe(board,i,j,str(k))):
                            board[i][j] = str(k)
                            numPossible = True
                            result = Solution.solveRecursive(self, board, i)
                            if(result == False):
                                board[i][j] = "."
                                numPossible = False
                    if(numPossible == False):
                        return False
                    return board

    def solveSudoku(self, board: List[List[str]]) -> None:
        res = self.solveRecursive(board)
        return res