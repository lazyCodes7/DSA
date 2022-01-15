class Solution:
    def solveRecursive(self, n):
        if(n == 1):
            return "1"
        else:
            number = Solution.solveRecursive(self, n-1)
            number = self.computeCountSay(number)
            
            return number
            
    def computeCountSay(self, number):
        temp = number[0]
        c = 0
        string = ""
        for i in number:
            if(i == temp):
                c+=1
            else:
                string+= str(c)+temp
                temp = i
                c=1
        
        string+=str(c)+temp
        return string
            
            
            
    def countAndSay(self, n: int) -> str:
        computed_number = self.solveRecursive(n)
        return computed_number