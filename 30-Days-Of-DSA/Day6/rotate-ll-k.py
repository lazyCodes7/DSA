# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        len_list = 0
        temp = head
        if(head != None):
            while(temp.next!=None):
                len_list+=1
                temp = temp.next
            len_list+=1
            rotation_amt = (len_list - k%len_list)%len_list -1
            if(rotation_amt>-1):
                temp1 = head
                while(rotation_amt>0):
                    temp1 = temp1.next
                    rotation_amt-=1

                newhead = temp1.next
                temp1.next = None
                temp.next = head

                return newhead
            return head
        else:
            return None