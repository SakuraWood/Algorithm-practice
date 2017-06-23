class Node(object):
    def __init__(self,k,l=None,r=None,p=None):
        self.lchild=l
        self.rchild=r
        self.parent=p
        self.key=k

    def has_left_child(self):
        return self.lchild
    
    def has_right_child(self):
        return self.rchild

    def is_left_child(self):
        return self.parent and self.parent.lchild==self

    def is_right_child(self):
        return self.parent and self.parent.rchild==self

class BinarySearchTree(object):
    def __init__(self):
        self.root=None
        self.node_size=0

    def length(self):
        return self.node_size

    def insert(self,x):
        node= Node(x)
        
