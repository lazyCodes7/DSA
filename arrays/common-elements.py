class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        i, j, k = 0, 0, 0
        ar1, ar2, ar3 = A, B, C 
        return_list = []
        last_element = -1
        
        flag = 0
     
    # Iterate through three arrays while all arrays have elements   
        while (i < n1 and j < n2 and k< n3):
             
            # If x = y and y = z, print any of them and move ahead
            # in all arrays
            if (ar1[i] == ar2[j] and ar2[j] == ar3[k]):
                if(last_element != ar1[i] or flag == 0):
                    flag = 1
                    return_list.append(ar1[i])
                last_element = ar1[i]
                i += 1
                j += 1
                k += 1
             
            # x < y   
            elif ar1[i] < ar2[j]:
                i += 1
                 
            # y < z   
            elif ar2[j] < ar3[k]:
                j += 1
             
            # We reach here when x > y and z < y, i.e., z is smallest   
            else:
                k += 1
        return return_list