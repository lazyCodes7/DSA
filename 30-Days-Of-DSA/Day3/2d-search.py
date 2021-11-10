class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowPresent = 0
        found = -1
        matrix_row_len = len(matrix)
        matrix_col_len = len(matrix[0])
        for i in range(matrix_row_len):
            print(matrix[i][matrix_col_len-1])
            if(target<=matrix[i][matrix_col_len-1]):
                rowPresent = i
                found = 1
                break
        if(found == -1):
            return False
        
        arr = matrix[rowPresent]
        high = matrix_col_len-1
        low = 0

        while(low<=high):
            mid = (high+low)//2
            if(arr[mid]>target):
                high = mid-1

            elif(arr[mid]<target):
                low = mid+1

            else:
                return True
        return False
        