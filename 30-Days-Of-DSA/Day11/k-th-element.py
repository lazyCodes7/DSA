def kthElement(arr1, arr2, n, m, k):
    if(len(arr1)>len(arr2)):
        arr1, arr2 = arr2, arr1
        
    l1 = len(arr1)
    l2 = len(arr2)

    print(l1,l2)
    
    low = 0
    high = l1
    
    while(low<=high):
        mid = (low+high)//2
        rem = k - mid
        print(rem)
        l1 = float('-inf') if mid<=0 else arr1[mid-1] 
        l2 = float('-inf') if rem<=0 else arr2[rem-1]
        
        print(rem, mid)
        print(rem == l2)
        r1 = float('inf') if mid==l1 else arr1[mid] 
        r2 = float('inf') if rem==l2 else arr2[rem]
        
        if(l1<=r2 and l2<=r1):
            return max(l1,l2)
            
        
        elif(l1>r2):
            high = mid-1
            
        elif(l2>r1):
            low = mid+1
print(kthElement([2],[3],1,1,1))

