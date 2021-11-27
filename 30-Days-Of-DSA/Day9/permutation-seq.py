class Solution:
    def solveRecursive(self, arr, return_list, k, n, arr_len):
        if(arr == []):
            return return_list
        else:
            index = k//n
            return_list.append(arr[index])
            del arr[index]
            arr_len-=1
            k = k%n
            if(arr_len>0):
                n = int(n/arr_len)
            Solution.solveRecursive(self, arr, return_list, k, n, arr_len)
        return return_list
            
            
    def getPermutation(self, n: int, k: int) -> str:
        permutations = 1
        for i in range(1,n+1):
            permutations = permutations*i
        arr = [j for j in range(1,n+1)]
        
        result = self.solveRecursive(arr, [], k-1, int(permutations/n), len(arr))
        ans = ""
        for elements in result:
            ans+=str(elements)
        return ans