class quake_node:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0
        self.item = None
        self.key = None
        
class quake_heap:
    def __init__(self):
        self.size = 0
        self.minimum = None
        self.highest_node = 0
        self.violation = None
        self.max_rank = 64
        self.alpha = 0.75
        self.roots = [None] * self.max_rank
        self.nodes = [0] * self.max_rank

    
    def pq_clear(self):
        self.size = 0
        self.minimum = None
        self.highest_node = 0
        self.violation = None
        self.roots = [None] * self.max_rank
        self.nodes = [0] * self.max_rank
    
    def pq_get_key(self, node):
        return node.key
    
    def pq_get_size(self):
        return self.size
    
    def pq_insert(self, item, key):
        wrapper = quake_node()
        wrapper.item = item
        wrapper.key = key
        wrapper.parent = wrapper
        self.size += 1
        self.make_root(wrapper)
        self.nodes[0] += 1
        return wrapper
    
    def pq_find_min(self):
        if self.pq_empty():
            return None
        return self.minimum
    
    def pq_delete_min(self):
        return self.pq_delete(self.minimum)
    
    def pq_delete(self, node):
        key = node.key
        self.cut(node)
        self.fix_roots()
        self.fix_decay()
        self.size -= 1
        return key
    
    def pq_decrease_key(self, node, new_key):
        node.key = new_key
        if self.is_root(node):
            if node.key < this.minimum.key:
                self.minimum = node
        else:
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
        self.make_root(node)
        
    def pq_meld(self, a, b):
        if a.size >= b.size:
            result = a
            trash = b
        else:
            result = b
            trash = a
        if trash.minimum == None:
            return result
        temp = result.minimum.parent
        result.minimum.parent = trash.minimum.parent
        trash.minimum.parent = temp
        for k in range(result.highest_node):
            result.nodes[k] += trash.nodes[k]
        return result
    
    def pq_empty(self):
        return self.size == 0
    
    def make_root(self, node):
        if node == None:
            return
        if self.minimum == None:
            self.minimum = node
            node.parent = node
        else:
            node.parent = self.minimum.parent
            self.minimum.parent = node
            
    def remove_from_roots(self, node):
        current = node.parent
        while current.parent != node:
            current = current.parent
        if current == node:
            self.minimum = None
        else:
            current.parent = node.parent
            if self.minimum == node:
                self.minimum = current
                
    def cut(self, node):
        if node == None:
            return

        if self.is_root(node):
            self.remove_from_roots(node)
        else:
            if node.parent.left == node:
                node.parent.left == None
            elif node.parent.right == node:
                node.parent.right = None
                
        self.cut(node.left)
        self.make_root(node.right)
        
        self.nodes[node.height] -= 1
        
    def join(self, a, b):
        if b.key < a.key:
            parent = b
            child = a
        else:
            parent = a
            child = b
        duplicate = self.clone_node(parent)
        if duplicate.left != None:
            duplicate.left.parent = duplicate
        if duplicate.right != None:
            duplicate.right.parent = duplicate
            
        duplicate.parent = parent
        child.parent = parent
        
        parent.parent = None
        parent.left = duplicate
        parent.right = child
        parent.height += 1
        self.nodes[parent.height] += 1
        
        return parent
    
    def fix_roots(self):
        if self.minimum == None:
            return
        
        for i in range(self.highest_node+1):
            self.roots[i] = None
        self.highest_node = 0
        
        current = self.minimum.parent
        tail = self.minimum
        self.minimum.parent = None
        
        while current != None:
            n = current.parent
            current.parent = None
            if not self.attempt_insert(current):
                height = current.height
                joined = self.join(current, self.roots[height])

                if current == tail:
                    tail = joined
                    n = tail
                else:
                    tail.parent = joined
                    tail = tail.parent
                self.roots[height] = None
            current = n
        
        head = None
        tail = None
        for i in range(self.highest_node+1):
            if self.roots[i] != None:
                if head == None:
                    head = self.roots[i]
                    tail = self.roots[i]
                else:
                    tail.parent = self.roots[i]
                    tail = tail.parent
        tail.parent = head
        self.minimum = head
        self.fix_min()
        
    def attempt_insert(self, node):
        height = node.height
        if self.roots[height] != None and self.roots[height] != node:
            return False
        if height > self.highest_node:
            self.highest_node = height
        self.roots[height] = node
        return True
    
    def fix_min(self):
        start = self.minimum
        current = self.minimum.parent
        while current != start:
            if current.key < self.minimum.key:
                self.minimum = current
            current = current.parent
    
    def fix_decay(self):
        self.check_decay()
        if self.violation_exists():
            for i in range(self.violation, self.max_rank):
                if self.roots[i] != None:
                    self.prune(self.roots[i])
                    
    def check_decay(self):
        i = 1
        for i in range(1, self.highest_node + 1):
            if self.nodes[i] > self.alpha * self.nodes[i-1]:
                break
        self.violation = i + 1 if i == self.highest_node else i
        
    def violation_exists(self):
        return self.violation < self.max_rank
    
    def prune(self, node):
        if node == None:
            return
        
        if node.height < self.violation:
            if not self.is_root(node):
                self.make_root(node)
            return
        
        duplicate = node.left
        child = node.right
        
        self.prune(child)
        
        node.left = duplicate.left
        if node.left != None:
            node.left.parent = node
        if node.right != None:
            node.right.parent = node
        
        self.nodes[node.height] -= 1
        node.height -=1
        
        self.prune(node)
        
    def clone_node(self, original):
        clone = quake_node()
        clone.item = original.item
        clone.key = original.key
        clone.left = original.left
        clone.right = original.right
        clone.height = original.height
        
        return clone
    
    def is_root(self, node):
        return node.parent.left != node and node.parent.right != node
