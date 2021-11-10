# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        len_list = 0
        temp = head
        while(temp != None):
            len_list+=1
            temp = temp.next
            
        temp = head
        n = len_list - n
        
        if(n == 0):
            temp = head.next
            head = temp
            
        elif(n == len_list-1):
            while(temp.next!=None):
                prev = temp
                temp = temp.next
            
            prev.next = None
            
        else:
            while(n>0):
                n-=1
                prev = temp
                temp = temp.next
                next_node = temp.next
            prev.next = next_node

        return head
        