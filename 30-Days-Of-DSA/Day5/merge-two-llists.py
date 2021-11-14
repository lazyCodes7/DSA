# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        temp = head
        len_list = 0
        temp_l1 = l1
        temp_l2 = l2
        while(temp_l1!=None):
            len_list+=1
            temp_l1 = temp_l1.next
            
        while(temp_l2!=None):
            len_list+=1
            temp_l2 = temp_l2.next
            
            
        if(len_list == 0):
            head = None
            
        else:
            len_list-=1
            while(len_list>0):
                node = ListNode(0)
                temp.next = node
                temp = temp.next
                len_list-=1

            temp = head

            while(l1!=None and l2!=None):
                if(l1.val>l2.val):
                    temp.val = l2.val
                    l2 = l2.next

                else:
                    temp.val = l1.val
                    l1 = l1.next

                temp = temp.next

            while(l1!=None):
                temp.val = l1.val
                l1 = l1.next
                temp = temp.next

            while(l2!=None):
                temp.val = l2.val
                l2 = l2.next
                temp = temp.next


            print(head)
            
        return head