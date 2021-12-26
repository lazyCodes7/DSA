# An efficient Python3 program to find
# maximum of all minimums of windows of
# different sizes
 
def printMaxOfMin(arr, n):
     
    s = [] # Used to find previous
           # and next smaller
 
    # Arrays to store previous and next
    # smaller. Initialize elements of
    # left[] and right[]
    left = [-1] * (n + 1)
    right = [n] * (n + 1)
 
    # Fill elements of left[] using logic discussed on
    # https:#www.geeksforgeeks.org/next-greater-element
    for i in range(n):
        while (len(s) != 0 and
               arr[s[-1]] >= arr[i]):
            s.pop()
 
        if (len(s) != 0):
            left[i] = s[-1]
 
        s.append(i)
 
    # Empty the stack as stack is going
    # to be used for right[]
    while (len(s) != 0):
        s.pop()
 
    # Fill elements of right[] using same logic
    for i in range(n - 1, -1, -1):
        while (len(s) != 0 and arr[s[-1]] >= arr[i]):
            s.pop()
 
        if(len(s) != 0):
            right[i] = s[-1]
 
        s.append(i)
 
    # Create and initialize answer array
    ans = [0] * (n + 1)
    for i in range(n + 1):
        ans[i] = 0
 
    # Fill answer array by comparing minimums
    # of all. Lengths computed using left[]
    # and right[]
    for i in range(n):
         
        # Length of the interval
        Len = right[i] - left[i] - 1
 
        # arr[i] is a possible answer for this
        #  Length 'Len' interval, check if arr[i]
        # is more than max for 'Len'
        ans[Len] = max(ans[Len], arr[i])
 
    # Some entries in ans[] may not be filled
    # yet. Fill them by taking values from
    # right side of ans[]
    for i in range(n - 1, 0, -1):
        ans[i] = max(ans[i], ans[i + 1])
 
    # Print the result
    for i in range(1, n + 1):
        print(ans[i], end = " ")
 
# Driver Code
if __name__ == '__main__':
 
    arr = [10, 20, 30, 50, 10, 70, 30]
    n = len(arr)
    printMaxOfMin(arr, n)