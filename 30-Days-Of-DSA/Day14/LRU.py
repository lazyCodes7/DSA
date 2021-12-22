class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        #print(self.hashmap)
        if(key in self.hashmap):
            node = self.hashmap[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            del self.hashmap[node.key]
            newNode = Node(node.key, node.val)
            newNode.next = self.head.next
            newNode.prev = self.head
            self.head.next.prev = newNode
            self.head.next = newNode
            self.hashmap[key] = newNode
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if(key in self.hashmap):
            node = self.hashmap[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            del self.hashmap[node.key]
            newNode = Node(node.key, value)
            newNode.next = self.head.next
            newNode.prev = self.head
            self.head.next.prev = newNode
            self.head.next = newNode
            self.hashmap[key] = newNode
        elif(len(self.hashmap)<self.capacity):
            newNode = Node(key,value)
            newNode.next = self.head.next
            newNode.prev = self.head
            self.head.next.prev = newNode
            self.head.next = newNode
            self.hashmap[key] = newNode
        elif(len(self.hashmap)>=self.capacity):
            #print("yes")

            leastUsed = self.tail.prev
            #print(leastUsed.key)
            leastUsed.prev.next = self.tail
            self.tail.prev = leastUsed.prev
            leastUsed.prev = None
            leastUsed.next = None
            del self.hashmap[leastUsed.key]
            newNode = Node(key,value)
            newNode.next = self.head.next
            newNode.prev = self.head
            self.head.next.prev = newNode
            self.head.next = newNode
            self.hashmap[key] = newNode
            #print(self.hashmap)

lRUCache = LRUCache(capacity = 2)
lRUCache.put(1,1)
lRUCache.put(1,1)
lRUCache.put(2, 2)
lRUCache.get(1)
lRUCache.put(3, 3)
lRUCache.get(2)
lRUCache.put(4, 4)
lRUCache.get(1)
lRUCache.get(3)
lRUCache.get(4)
print(lRUCache.hashmap)