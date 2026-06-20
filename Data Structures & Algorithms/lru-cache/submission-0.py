class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next =None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, key, value):
        node = ListNode(key, value)

        if not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        return node

    def delete(self, node):
        if not self.head:
            return
        
        if self.head == node:
            self.head = self.head.next

            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return
        
        if self.tail == node:
            self.tail = self.tail.prev

            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            return

        if node.next and node.prev:
            node.next.prev = node.prev
            node.prev.next = node.next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = {}
        self.dll = DLL()

    def get(self, key: int) -> int:

        if key in self.lru:
            node = self.lru[key]
            val = node.value

            self.dll.delete(node)
            self.lru[key] = self.dll.insert(key,val)

            return val

        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            node = self.lru[key]
            self.dll.delete(node)
        self.lru[key] = self.dll.insert(key,value)

        if len(self.lru) > self.capacity:
            key = self.dll.head.key
            self.lru.pop(key)
            self.dll.delete(self.dll.head)        
