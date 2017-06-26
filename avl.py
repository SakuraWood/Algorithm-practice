class Node(object):
    def __init__(self,k,l=None,r=None,p=None):
        self.lchild=l
        self.rchild=r
        self.parent=p
        self.key=k
        self.bf=0
        self.height=0

    def get_bf(self):
        return self.bf

    def get_height(self):
        return self.height
    
    def set_height(self,h):
        self.height=h
        
    def has_left_child(self):
        return self.lchild
    
    def has_right_child(self):
        return self.rchild

    def is_left_child(self):
        return self.parent and self.parent.lchild==self

    def is_right_child(self):
        return self.parent and self.parent.rchild==self

class AVLTree(object):
    def __init__(self):
        self.root=None
        self.node_size=0

    def length(self):
        return self.node_size

    def insert(self,x):
        node= Node(x)
        if not self.root:
            self.root=node
            self.node_size=1
        else:
            current_node=self.root
            while True:
                if x<current_node.key:                      #x如果小于当前节点的key，则想办法弄到左边
                    if current_node.lchild:
                        current_node=current_node.lchild
                    else:
                        current_node.lchild=node
                        node.parent=current_node
                        self.node_size+=1
                        break
                elif x>current_node.key:
                    if current_node.rchild:
                        current_node=current_node.rchild
                    else:
                        current_node.rchild=node
                        node.parent=current_node
                        self.node_size+=1
                        break
                else:
                    break

    def find(self,x):
        current_node=self.root
        while True:
            if not current_node:
                result=None
                break
            elif x<current_node.key:
                current_node=current_node.lchild
            elif x>current_node.key:
                current_node=current_node.rchild
            else:
                result=current_node
                break
        return result

    def get_successor(self,x):
        node=self.find(x)
        current_node=node.rchild
        while current_node.lchild:
            current_node=current_node.lchild
        return current_node

    def get_pre(self,x):
        node=self.find(x)
        current_node=node.lchild
        while current_node.rchild:
            current_node=current_node.rchild
        return current_node

    def remove(self,x):
        self.delete(x)
        self.node_size-=1

    def delete(self,x):
        node=self.find(x)
        try:
            if node.lchild and not node.rchild:
                pre=self.get_pre(node.key)
                value=pre.key
                self.delete(value)
                node.key=value
            elif node.rchild and not node.lchild:
                if node.is_left_child():
                    node.rchild.parent=node.parent
                    node.parent.lchild=node.rchild
                else:
                    node.rchild.parent=node.parent
                    node.parent.rchild=node.rchild
                # value=node.rchild.key
                # self.delete(value)
                # node.key=value
            elif node.lchild and node.rchild:
                successor=self.get_successor(node.key)
                value=successor.key
                self.delete(value)
                node.key=value
            elif not node.lchild and not node.rchild:
                if node.is_left_child():
                    node.parent.lchild=None
                elif node.is_right_child():
                    node.parent.rchild=None
                else:
                    self.root=None
            else:
                raise AttributeError
        except AttributeError:
            print "The node is not in the tree"

def test():
    bst=BinarySearchTree()
    bst.insert(8)
    bst.insert(3)
    bst.insert(4)
    bst.insert(5)
    bst.insert(7)
    bst.insert(6)
    bst.insert(11)
    bst.insert(9)

    bst.remove(11)
    bst.remove(9)
    bst.remove(3)
    bst.remove(4)
    bst.remove(5)
    bst.remove(6)
    bst.remove(7)
    bst.remove(8)


    bst.insert(12)
    bst.insert(32)
    bst.insert(5)

test()