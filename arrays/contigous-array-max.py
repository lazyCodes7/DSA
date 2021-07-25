
class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,a,size):
        max_so_far = 0
        max_till_here = 0
        
        for i in range(size):
            max_till_here+=a[i]
            if(max_till_here > max_so_far):
                max_so_far = max_till_here
            if(max_till_here<0):
                max_till_here=0
        if(max_so_far == 0):
            max_so_far = max(a)
        return max_so_far
        


import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
