class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = 1
        r = len(nums)-1
        i = 0
        lenN = len(nums)
        isFound = {}
        ans = []
        a = nums
        a.sort()
        #print(a)
        
        while(i<lenN-2):
            l = i+1
            r = lenN-1
            while(l<r):
                sum = a[i]+a[l]+a[r]
                #print(sum)
                if(sum>0):
                    r-=1
                elif(sum<0):
                    l+=1
                elif(sum == 0):
                    key = frozenset([a[i],a[l],a[r]])
                    if key not in isFound:
                        ans.append([a[i],a[l],a[r]])
                        isFound[key] = True
                    l+=1
                    r-=1
            i+=1
        return ans