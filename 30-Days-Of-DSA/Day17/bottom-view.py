#User function Template for python3
from queue import Queue
from collections import OrderedDict

class Solution:
    def bottomView(self, root):
        line_map = OrderedDict()
        q = Queue()
        q.put((root, 0))
        line_map[0] = root.data
        idx = 0
        while(q.empty() == False):
            curr = q.get()
            node, line_level = curr
            if(node.left != None):
                q.put((node.left, line_level-1))
                line_map[line_level-1] = node.left.data
            if(node.right != None):
                q.put((node.right, line_level+1))
                line_map[line_level+1] = node.right.data
                
        min_key = min(list(line_map.keys()))
        
        ans = []
        while(min_key in line_map):
            ans.append(line_map[min_key])
            min_key+=1
                
        return ans