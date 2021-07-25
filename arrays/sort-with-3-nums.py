array = list(map(int, input().split()))

def sort012(arr,n):
    arr_0 = []
    arr_1 = []
    arr_2 = []
    j_counter = 0
    k_counter = 0
    m_counter = 0
    r_arr = []
    for i in range(n):
	    if(arr[i]//2 == 0 and arr[i]%2 == 0):
	        arr_0.append(0)
	    elif(arr[i]%2 == 1):
	        arr_1.append(1)
	    elif(arr[i]//2 == 1):
	        arr_2.append(2)
    for i in range(n):
        if(j_counter < len(arr_0)):
            r_arr.append(arr_0[j_counter])
            j_counter+=1
        elif(k_counter < len(arr_1)):
            r_arr.append(arr_1[k_counter])
            k_counter+=1
        elif(m_counter < len(arr_1)):
            r_arr.append(arr_2[m_counter])
            m_counter+=1
    
    return r_arr
print(sort012(array, len(array)))