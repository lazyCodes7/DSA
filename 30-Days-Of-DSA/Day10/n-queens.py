import copy
class Solution:
    def isSafe(self, row, column, chess_list, n):
        temp_row = row-1
        temp_column = column-1
        
        while(temp_row >= 0 and temp_column>=0):
            if(chess_list[temp_row][temp_column] == "Q"):
                return False
            temp_row-=1
            temp_column-=1
            
        temp_row = row-1
        temp_column = column+1
        
        while(temp_row>=0 and temp_column<n):
            if(chess_list[temp_row][temp_column] == "Q"):
                return False
            temp_row-=1
            temp_column+=1
            
        temp_row = row-1
        temp_column = column
        
        while(temp_row>=0):
            if(chess_list[temp_row][temp_column] == "Q"):
                return False
            temp_row-=1
        
        return True
        
    def solveRecursive(self, n, i, chess_list, return_list):
        if(i == len(chess_list)):
            temp_list = []
            for elements in chess_list:
                string = "".join(elements)
                temp_list.append(string)
            return_list.append(temp_list)

        else:
            column = chess_list[i]
            for j in range(len(column)):
                if(self.isSafe(i,j,chess_list,n)):
                    chess_list[i][j] = "Q"
                    Solution.solveRecursive(self,n,i+1,chess_list,return_list)
                    chess_list[i][j] = "."
        return return_list
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        required_list = []
        string = ""
        for j in range(n):
            string+="."
        for i in range(n):
            required_list.append(list(string))
        res = self.solveRecursive(n,0,required_list,[])
        return res