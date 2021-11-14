# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prev = None
        len_list = 0
        
        first_head = None
        
        flag = 1
        prevhead = None
        
        
        while(temp!=None):
            len_list+=1
            temp = temp.next
            
        index = (len_list//k)*k
        i = 0
        temp = head
        while(temp != None and index>0):
            if(i == 0):
                storehead = temp
                
            if(i!=k):
                curr = temp.next
                temp.next = prev
                #print(curr)
                prev = temp
                temp = curr
                #print(prev)
                i+=1
                
            if(i == k):
                print(prev)
                if(flag):
                    first_head = prev
                    flag = 0
                if(prevhead == None):
                    prevhead = storehead
                    storehead.next = temp
                    
                else:
                    prevhead.next = prev
                    prevhead = storehead
                    storehead.next = temp
                prev = None
                i = 0
            index-=1
        return first_head