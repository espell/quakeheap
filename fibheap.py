
class Fib_Node:
    def __init__(self):
        self.parent = None
        self.first_child = None
        self.next_sibling = None
        self.prev_sibling = None
        self.rank = 0
        self.marked = False
        self.item = None
        self.key = None

class Fib_Heap:
    def __init__(self):
        #don't need memory map anymore
        self.size = 0
        self.minimum = None #pointer to minimum node
        self.roots = [None for i in range(64)] #array of roots of the queue, USING MAXRANK VAL
        self.largest_rank = None #largest rank in the queue

    def pq_create(self):
        return Fib_Heap()

    def pq_get_key(self, queue, node):
        return node.key

    def pq_get_item(self,queue, node):
        return node.item

    def pq_get_size(self,queue):
        return queue.size

    def pq_insert(self,queue, item, key):
        queue.size = queue.size + 1
        wrapper = Fib_Node()
        wrapper.key = key
        wrapper.next_sibling = wrapper
        wrapper.prev_sibling = wrapper
        wrapper.item = item
        queue.minimum = self.append_lists(queue, queue.minimum, wrapper)
        return wrapper

    def pq_find_min(self,queue):
        if(self.pq_empty(queue)):
            return None
        return queue.minimum

    def pq_delete_min(self,queue):
        node = queue.minimum
        key = node.key
        child = node.first_child

        #remove from sibling list
        node.next_sibling.prev_sibling = node.prev_sibling
        node.prev_sibling.next_sibling = node.next_sibling

        #find new temp min
        if(node.next_sibling != node):
            queue.minimum = node.next_sibling
        else:
            queue.minimum = child

        #don't need to free node?

        queue.size = queue.size - 1
        self.merge_and_fix_roots(queue, queue.minimum, child)

        return key

    def pq_delete(self,queue, node):
        if(node == queue.minimum):
            return self.pq_delete_min(queue)

        key = node.key
        child = node.first_child

        #remove from sibling list
        node.next_sibling.prev_sibling = node.prev_sibling
        node.prev_sibling.next_sibling = node.next_sibling

        if(node.parent != None):
            node.parent.rank = node.parent.rank - 1

            if(node.parent.first_child ==node):
                if(node.parent.rank == 0):
                    node.parent.first_child = None
                else:
                    node.parent.first_child = node.next_sibling

            if(node.parent.marked == False):
                node.parent.marked = True
            else:
                self.cut_from_parent(queue, node.parent)

        #don't need to free Fib_Node
        queue.size = queue.size - 1
        self.append_lists(queue, queue.minimum, child)

        return key

    def pq_decrease_key(self,queue, node, new_key):
        node.key = new_key
        self.cut_from_parent(queue, node)

    def pq_empty(self,queue):
        return (queue.size == 0)
    
    def pq_meld(self, queue, trash):
        if trash.minimum == None:
            return self
        self.size += trash.size
        self.append_lists(queue, queue.minimum, trash.minimum)
        return self

    #### originally static methods in C implementation ####

    def merge_and_fix_roots(self,queue, a, b):
        start = self.append_lists(queue,a,b)
        current = Fib_Node()
        next = Fib_Node()

        if(start == None):
            return

        #break the circular append_list
        start.prev_sibling.next_sibling = None
        start.prev_sibling = None
        #insert initial Fib_Node
        queue.roots[start.rank] = start
        queue.largest_rank = start.rank
        start.parent = None
        current = start.next_sibling

        #insert the rest of the nodes
        while( current != None):
            next = current.next_sibling
            if(next != None):
                next.prev_sibling = None
            current.next_sibling = None
            current.parent = None

            while(not self.attempt_insert(queue, current)):
                rank = current.rank
                current = self.link(queue, current, queue.roots[rank])
                queue.roots[rank] = None

            current = next

        start = queue.roots[queue.largest_rank]
        queue.roots[queue.largest_rank] = None
        queue.minimum = start

        current = start
        for i in range(queue.largest_rank-1,0,-1):
            if(queue.roots[i] != None):
                if(queue.roots[i].key < queue.minimum.key):
                    queue.minimum = queue.roots[i]
                current.prev_sibling = queue.roots[i]
                queue.roots[i].next_sibling = current
                current = queue.roots[i]
                queue.roots[i] = None

        current.prev_sibling = start
        start.next_sibling = current
        queue.largest_rank = 0

    def link(self,queue, a, b):
        parent = None
        child = None
        if(b.key < a.key):
            parent = b
            child = a
        else:
            parent = a
            child = b

        child.marked = False
        child.parent = parent
        child.next_sibling = child
        child.prev_sibling = child
        parent.first_child = self.append_lists(queue, parent.first_child, child)
        parent.rank = parent.rank + 1

        return parent

    def cut_from_parent(self,queue, node):
        next = None
        prev = None

        if(node.parent != None):
            next = node.next_sibling
            prev = node.prev_sibling

            next.prev_sibling = node.prev_sibling
            prev.next_sibling = node.next_sibling

            node.next_sibling = node
            node.prev_sibling = node

            node.parent.rank = node.parent.rank -1
            if(node.parent.first_child == node):
                if(node.parent.rank == 0):
                    node.parent.first_child = None
                else:
                    node.parent.first_child = next

            if(node.parent.marked == False):
                node.parent.marked = True
            else:
                self.cut_from_parent(queue,node.parent)

            queue.minimum = self.append_lists(queue, node, queue.minimum)
            node.parent = None
        else:
            if(node.key < queue.minimum.key):
                queue.minimum = node

    def append_lists(self,queue, a, b):
        list = None
        a_prev = None
        b_prev = None

        if(a == None):
            list = b
        elif ((b == None) or (a==b)):
            list = a
        else:
            a_prev = a.prev_sibling
            b_prev = b.prev_sibling

            a_prev.next_sibling = b
            b_prev.next_sibling = a

            a.prev_sibling = b_prev
            b.prev_sibling = a_prev

            if(a.key <= b.key):
                list = a
            else:
                list = b
        return list

    def attempt_insert(self,queue, node):
        rank = node.rank
        occupant = queue.roots[rank]
        if((occupant != None) and (occupant != node)):
            return False

        queue.roots[rank] = node
        if(rank > queue.largest_rank):
            queue.largest_rank = rank

        return True
