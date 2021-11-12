# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodes = []
        len_list = 0
        
        temp = head
        while(temp!=None):
            len_list+=1
            temp = temp.next
            
            
        if(len_list == 1):
            return True
            
        elif(len_list%2==0):
            traverse_till = int((len_list-1)/2)
            
        else:
            traverse_till = int(len_list/2)
            
        temp = head
        while(traverse_till >= 0):
            nodes.append(temp.val)
            temp = temp.next
            traverse_till-=1
            
        if(len_list%2 != 0):
            nodes.pop()
            
        while(temp!=None):
            value = nodes.pop()
            if(value!=temp.val):
                return False
            
            temp = temp.next
            
        return True