class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class CircularDoublyLinkedList:
    def __init__(self):
        self.first=None
    def get_node(self,index):
        cur=self.first
        for i in range(index):
            cur=cur.next
            if cur==self.first:
                return None
        return cur
    def insert_at_end(self, new_node):
        if self.first is None:
            self.first = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.insert_after(self.first.prev, new_node)
    def insert_before(self, ref_node, new_node):
        self.insert_after(ref_node.prev, new_node)
        
    def insert_at_beg(self, n_node):
        self.insert_at_end(n_node)
        self.first = new_node
    def insert_after(self,r_node,n_node):
        n_node.prev=r_node
        n_node.next=r_node.next
        n_node.next.prev=n_node
        r_node.next=n_node
        
