# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseRecursive(self, head, prev = None):
        if(head == None):
            return prev
        temp = head.next
        head.next = prev
        prev = head
        return Solution.reverseRecursive(self, temp, prev)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newhead = self.reverseRecursive(head)
        return newhead