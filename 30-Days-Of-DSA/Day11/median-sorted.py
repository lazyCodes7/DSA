import sys
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if(len(nums2)<len(nums1)):
            nums1, nums2 = nums2, nums1
            
        len_1 = len(nums1)
        len_2 = len(nums2)
        
        low = 0
        high = len_1
        length = (len_1+len_2+1)//2
        if(nums1 == []):
            if(len_2%2 == 0):
                return (nums2[len_2//2] + nums2[(len_2//2)-1]) / 2.0
            else:
                return nums2[len_2//2]
                
        while(low<=high):
            cut1 = (low+high)//2
            cut2 = length - cut1
            
            l1 = float('-inf') if cut1 <= 0 else nums1[cut1-1]
            l2 = float('-inf') if cut2 <= 0 else nums2[cut2-1]
            
            r1 = float('inf') if cut1 >= len_1 else nums1[cut1]
            r2 = float('inf') if cut2 >= len_2 else nums2[cut2]

            if(l1<=r2 and l2<=r1):

                if((len_1+len_2)%2 == 0):
                    return (max(l1,l2) + min(r1, r2))/2
                else:
                    return max(l1,l2)
                
            elif(l1>r2):
                high = cut1-1
            
            elif(l1<r2):
                low = cut1+1
                
        return 0.0