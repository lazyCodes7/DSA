#Function to return the count of number of elements in union of two arrays.
def doUnion(self,a,n,b,m):
    union_set = set(a+b)
    return_list = list(union_set)
    
    return len(return_list)
        

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        
        print(ob.doUnion(a,n,b,m))
# } Driver Code Ends