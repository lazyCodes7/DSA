def solveRecursive(arr):
    swaps = 0
    if(len(arr) == 1):
        return swaps
    else:
        left = 0
        right = len(arr)
        mid = (left+right)//2
        swaps += solveRecursive(arr[left:mid])
        swaps += solveRecursive(arr[mid:right])
        swaps += merge(arr, left, mid, right)
    
        return swaps

def solveRevRecursive(arr):
    print(arr)
    swaps = 0
    if(len(arr) == 1):
        return swaps
    else:
        left = 0
        right = len(arr)
        mid = (left+right)//2
        swaps += solveRevRecursive(arr[left:mid])
        swaps += solveRevRecursive(arr[mid:right])
        swaps += merge_reverse(arr, left, mid, right)
    
        return swaps
    
def merge_reverse(arr, left, mid, right):
    print(arr)
    new_arr = []
    arr1 = arr[left:mid]
    arr2 = arr[mid:right]
    i = 0
    j = 0
    swaps = 0
    while(i<len(arr1) and j<len(arr2)):
        if(arr1[i] < arr2[j]):
            new_arr.append(arr2[j])
            swaps+=1
            j+=1
        else:
            new_arr.append(arr1[i])
            i+=1
    while(i<len(arr1)):
        new_arr.append(arr1[i])
        i+=1
    while(j<len(arr2)):
        new_arr.append(arr2[j])
        j+=1
    arr[left:right] = new_arr
    return swaps

def merge(arr, left, mid, right):
    new_arr = []
    arr1 = arr[left:mid]
    arr2 = arr[mid:right]
    i = 0
    j = 0
    swaps = 0
    while(i<len(arr1) and j<len(arr2)):
        if(arr1[i] > arr2[j]):
            new_arr.append(arr2[j])
            swaps+=1
            j+=1
        else:
            new_arr.append(arr1[i])
            i+=1
    while(i<len(arr1)):
        new_arr.append(arr1[i])
        i+=1
    while(j<len(arr2)):
        new_arr.append(arr2[j])
        j+=1
    arr[left:right] = new_arr
    return swaps
def lilysHomework(arr):
    swaps = solveRecursive(arr)
    rev_swaps = solveRevRecursive(arr)
    print(rev_swaps)
    return min(swaps, rev_swaps)
    # Write your code here

print(lilysHomework([2,5,3,1]))