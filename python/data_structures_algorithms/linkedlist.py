class _SingleNode:
    
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
        
    def get_next(self):
        return self.next_node
    
    def set_next(self, node):
        self.next_node = node
        
    def __str__(self):
        return(str(self.value))
        
class SinglyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
        
    def count(self):
        return self.len
    
    def clear(self):
        self.head = None
        self.tail = None
        self.len = 0
    
    def append(self, value):
        if self.count() == 0:
            node = _SingleNode(value)
            self.head = node
            self.tail = node
            self.len += 1
        else:
            node = _SingleNode(value)
            self.tail.set_next(node)
            self.tail = node
            self.len += 1
            
    def traverse(self):
        curr_node = self.head
        while curr_node != None:
            print(curr_node)
            curr_node = curr_node.get_next()
            
    def extend(self, iterable):
        for item in iterable:
            self.append(item)
            
        
    
        