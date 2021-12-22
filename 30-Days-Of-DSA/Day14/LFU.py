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

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.freq_map = {}
        self.least_freq = 0
        self.curr_capacity = 0
        self.hashmap = {}

    def get(self, key: int) -> int:
        if(key in self.hashmap):
            node, freq = self.hashmap[key][0], self.hashmap[key][1]
            if(freq+1 in self.freq_map):
                self.freq_map[freq+1].put(node.key, node.val)
                self.hashmap[key] = [self.freq_map[freq+1].hashmap[key], freq+1]
            else:
                self.freq_map[freq+1] = LRUCache(capacity = self.capacity)
                self.freq_map[freq+1].put(node.key, node.val)
                self.hashmap[key] = [self.freq_map[freq+1].hashmap[key], freq+1]

            remove_key = self.freq_map[freq].hashmap[key]
            remove_key.prev.next = remove_key.next
            remove_key.next.prev = remove_key.prev
            remove_key.prev = None
            remove_key.next = None
            del self.freq_map[freq].hashmap[remove_key.key]
            #print(self.freq_map[self.least_freq].hashmap)
            if(self.freq_map[self.least_freq].hashmap == {}):
                self.least_freq = freq+1
            return node.val
        return -1





    def put(self, key: int, value: int) -> None:
        if(key in self.hashmap):
            node, freq = self.hashmap[key][0], self.hashmap[key][1]
            if(freq+1 in self.freq_map):
                self.freq_map[freq+1].put(key, value)
                self.hashmap[key] = [self.freq_map[freq+1].hashmap[key], freq+1]
            else:
                self.freq_map[freq+1] = LRUCache(capacity = self.capacity)
                self.freq_map[freq+1].put(key, value)
                self.hashmap[key] = [self.freq_map[freq+1].hashmap[key], freq+1]

            remove_key = self.freq_map[freq].hashmap[key]
            remove_key.prev.next = remove_key.next
            remove_key.next.prev = remove_key.prev
            remove_key.prev = None
            remove_key.next = None
            del self.freq_map[freq].hashmap[remove_key.key]
            #print(self.freq_map[self.least_freq].hashmap)
            if(self.freq_map[self.least_freq].hashmap == {}):
                self.least_freq = freq+1


        elif(self.curr_capacity < self.capacity):
            self.least_freq = 1
            if(self.least_freq not in self.freq_map):
                self.freq_map[self.least_freq] = LRUCache(capacity = self.capacity)
                self.freq_map[self.least_freq].put(key, value)
            else:
                self.freq_map[self.least_freq].put(key, value)

            self.hashmap[key] = [self.freq_map[self.least_freq].hashmap[key], self.least_freq]
            self.curr_capacity+=1

        elif(self.curr_capacity >= self.capacity):
            print(self.least_freq)
            leastUsed = self.freq_map[self.least_freq].tail.prev
            #print(leastUsed.key)
            leastUsed.prev.next = self.freq_map[self.least_freq].tail
            self.freq_map[self.least_freq].tail.prev = leastUsed.prev
            leastUsed.prev = None
            leastUsed.next = None
            del self.freq_map[self.least_freq].hashmap[leastUsed.key]
            del self.hashmap[leastUsed.key]

            self.least_freq = 1
            if(self.least_freq not in self.freq_map):
                self.freq_map[self.least_freq] = LRUCache(capacity = self.capacity)
                self.freq_map[self.least_freq].put(key, value)
                self.hashmap[key] = [self.freq_map[self.least_freq].hashmap[key], self.least_freq]
            else:
                self.freq_map[self.least_freq].put(key, value)
                self.hashmap[key] = [self.freq_map[self.least_freq].hashmap[key], self.least_freq]

            

cache = LFUCache(capacity = 2)
cache.put(1,1)
cache.put(2,2)
cache.get(1)
cache.put(3,3)
cache.get(2)
cache.get(3)
cache.put(4,4)
cache.get(1)
cache.get(3)
cache.get(4)

print(cache.least_freq)            
print(cache.hashmap)
print(cache.freq_map[1].hashmap)
print(cache.freq_map[2].hashmap)
print(cache.freq_map[3].hashmap)

