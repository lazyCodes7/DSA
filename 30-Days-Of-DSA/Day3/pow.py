class Solution:
    def myPow(self, x: float, n: int) -> float:
        if(n==1):
            return x
        elif(n==-1):
            return 1/x
      
        elif(n == 0):
            return 1
        else:
            if(n>0):
                if(n%2==0):
                    res = Solution.myPow(self,x*x, int(n/2))
                else:
                    res = float(x)*Solution.myPow(self,x,n-1)
                
            else:
                if(n%2==0):
                    res = Solution.myPow(self,x*x,int(n/2))
                else:
                    res = (1/x)*Solution.myPow(self,x,n+1)
        return res
        