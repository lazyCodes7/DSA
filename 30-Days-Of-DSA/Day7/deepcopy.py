"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if(head == None):
            return None
        node = Node(head.val)
        temp = node
        init_temp = head
        visited_address = {}
        
        while(init_temp!=None):
            visited_address[init_temp] = temp
            if(init_temp.next!=None):
                next_val = init_temp.next.val
                temp.next = Node(next_val)
                
            else:
                temp.next = None
            
            init_temp = init_temp.next
            temp = temp.next
            
        temp = node
        init_temp = head
        
        while(init_temp!=None):
            if(init_temp.random!=None):
                random_val = init_temp.random.val
                temp.random = visited_address[init_temp.random]
            else:
                temp.random = None

            temp = temp.next
            init_temp = init_temp.next
        return node