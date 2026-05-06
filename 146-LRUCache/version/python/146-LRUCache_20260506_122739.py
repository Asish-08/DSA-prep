# Last updated: 5/6/2026, 12:27:39 PM
class Node:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.right = self.tail
        self.tail.left = self.head
        self.lookup = {}

    def add_node(self, node):
        prev_node = self.tail.left
        prev_node.right = node
        self.tail.left = node
        node.left = prev_node
        node.right = self.tail
        return node
    
    def remove_node(self, node):
        prev_node, next_node = node.left, node.right
        prev_node.right = next_node
        next_node.left = prev_node
        

    def get(self, key: int) -> int:
        if key not in self.lookup: return -1

        node = self.lookup[key]
        self.remove_node(node)

        new_node = Node(node.key, node.val)
        new_node = self.add_node(new_node)
        self.lookup[key] = new_node
        return new_node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            node = self.lookup[key]
            self.remove_node(node)
            del self.lookup[key]
        
        node = Node(key, value)
        node = self.add_node(node)
        self.lookup[key] = node

        if len(self.lookup)>self.capacity:
            to_remove = self.head.right
            self.remove_node(to_remove)
            del self.lookup[to_remove.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)