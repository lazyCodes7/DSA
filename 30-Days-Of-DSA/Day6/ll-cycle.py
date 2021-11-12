# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        temp = head
        while(temp!=None):
            try:
                if(visited[temp] == True):
                    return True
            except:
                pass
            visited[temp] = True
            temp = temp.next
            
        return False
        