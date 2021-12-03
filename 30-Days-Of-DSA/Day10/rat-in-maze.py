#User function Template for python3
import copy 
class Solution:
    def solveRecursive(self, i, j, m, n, return_list, temp_list, visited, choices):
        try:
            if(i<0 or j<0):
                return 
            if(i>=n or j>=n):
                return
                
            elif(m[i][j] == 0):
                return 
                
            elif(visited[i][j] == True):
                return 
                
            elif(i == n-1 and j == n-1):
                subset = "".join(temp_list)
                return_list.append(subset)
            else:
                for choice in choices:
                    if(choice == "D"):
                        visited[i][j] = True
                        temp_list.append(choice)
                        Solution.solveRecursive(self,i+1, j, m, n, return_list, temp_list, visited, choices)
                        visited[i][j] = False
                        temp_list.pop()
                    elif(choice == "L"):
                        visited[i][j] = True
                        temp_list.append(choice)
                        Solution.solveRecursive(self,i, j-1, m, n, return_list, temp_list, visited, choices)
                        visited[i][j] = False
                        temp_list.pop()
                    elif(choice == "R"):
                        visited[i][j] = True
                        temp_list.append(choice)
                        result = Solution.solveRecursive(self,i, j+1, m, n, return_list, temp_list, visited, choices)
                        visited[i][j] = False
                        temp_list.pop()
                    elif(choice == "U"):
                        visited[i][j] = True
                        temp_list.append(choice)
                        Solution.solveRecursive(self,i-1, j, m, n, return_list, temp_list, visited, choices)
                        visited[i][j] = False
                        temp_list.pop()
        except Exception as e:
            print(i)
            print(j)
            print(e)
        return return_list
        
                
        
    def findPath(self, m, n):
        choices = ["D", "L", "R", "U"]
        visited = [[False for i in range(n)] for j in range(n)]
        result = self.solveRecursive(0, 0, m, n, [], [], visited, choices)
        
        #print(len(result))
        if(result == None):
            return []
        return result