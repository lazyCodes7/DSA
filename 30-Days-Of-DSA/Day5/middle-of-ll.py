# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len_list = 0
        temp = head
        while(temp != None):
            len_list+=1
            temp = temp.next
            
        if(len_list%2==0):
            middle = int((len_list-1)/2) + 1
            
        else:
            middle = int(len_list/2)
            
        temp = head
        
        while(temp!=None and middle>0):
            temp = temp.next
            middle-=1
            
        return temp