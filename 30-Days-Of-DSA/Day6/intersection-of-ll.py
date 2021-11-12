# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_temp = l1
        l2_temp = l2
        len_l1 = 0
        len_l2 = 0
        
        while(l1_temp!=None):
            len_l1+=1
            l1_temp = l1_temp.next
        
        while(l2_temp!=None):
            len_l2+=1
            l2_temp = l2_temp.next
            
        len_l1_l2 = max(len_l1, len_l2)
        len_l1_l2-=1
        newhead = ListNode(0)
        temp = newhead
        while(len_l1_l2 > 0):
            node = ListNode(0)
            temp.next = ListNode(0)
            temp = temp.next
            len_l1_l2-=1
            
        l1_temp = l1
        l2_temp = l2
        temp = newhead
        while(l1_temp!=None or l2_temp!=None):
            if(l1_temp!=None and l2_temp!=None):
                add = l1_temp.val + l2_temp.val
                l1_temp = l1_temp.next
                l2_temp = l2_temp.next
            elif(l2_temp == None):
                add = l1_temp.val
                l1_temp = l1_temp.next                
            else:
                add = l2_temp.val
                l2_temp = l2_temp.next

                
            if(add>9):
                add_split = list(str(add))
                carry, digit = int(add_split[0]), int(add_split[1])
                temp.val = digit
                if(l1_temp!=None):
                    l1_temp.val+=carry
                    
                elif(l2_temp!=None):
                    l2_temp.val+=carry
                    
                else:
                    temp.next = ListNode(carry)
                    
                temp = temp.next
                    
            else:
                temp.val = add
                temp = temp.next
                
        return newhead
                    
                
                    
        