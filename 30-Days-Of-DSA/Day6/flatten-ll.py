'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

def flatten(root):
    if(root == None):
        return root
        
    else:
        res = flatten(root.next)
        merged_ll = merge(root, res)
        
        return merged_ll
        
def merge(root1, root2):
    node = Node(0)
    temp = node
    temp1 = root1
    temp2 = root2
    
    while(temp1!=None and temp2!=None):
        if(temp1.data > temp2.data):
            temp.bottom = Node(temp2.data)
            temp = temp.bottom
            temp2 = temp2.bottom
            
        else:
            temp.bottom = Node(temp1.data)
            temp = temp.bottom
            temp1 = temp1.bottom
            
    while(temp1!=None):
        temp.bottom = Node(temp1.data)
        temp = temp.bottom
        temp1 = temp1.bottom
        
    while(temp2!=None):
        temp.bottom = Node(temp2.data)
        temp = temp.bottom
        temp2 = temp2.bottom
        
    return node.bottom