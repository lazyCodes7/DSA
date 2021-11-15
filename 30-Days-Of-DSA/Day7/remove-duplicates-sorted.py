class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = nums
        if(len(a) > 0):
            element = a[0]
            i = 0
            k = 0
            while(i<len(a)):
                if(a[i] == element):
                    i+=1

                else:
                    k+=1
                    element = a[i]
                    a[k] = a[i]
                    i+=1

            return k+1