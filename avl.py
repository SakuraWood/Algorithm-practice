#!/usr/bin/python
# -*- coding: UTF-8 -*-
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


class AVLTree(object):
    def __init__(self):
        self.root=None
        self.node_size=0

    def length(self):
        return self.node_size

    def is_balance(self,node):                     #判断是否平衡
        bf=self.get_bf(node)
        if bf>1 or bf<-1:
            return False
        else:
            return True

    def get_bf(self,node):                      #获取一个节点的平衡因子
        lh=self.get_node_h(node.lchild)
        rh=self.get_node_h(node.rchild)
        return lh-rh

    def get_node_h(self,node):                  #获取一个节点的高度
        return self.get_node_h_helper(node)-1

    def get_node_h_helper(self,node):           #获取高度的辅助函数
        l,r=0,0
        if node:
            l=self.get_node_h_helper(node.lchild)
            r=self.get_node_h_helper(node.rchild)
        return l+1 if l>r else r+1

    def insert(self,x):
        self.insert_helper(x)
        node=self.find(x)
        self.check_imbanlance(node)
    
    def insert_helper(self,x):
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
        node=self.find(x)
        self.delete(node)
        need_to_check_balance=node
        while need_to_check_balance:
            temp_parent=need_to_check_balance.parent
            self.check_imbanlance(need_to_check_balance)
            need_to_check_balance=temp_parent
        self.node_size-=1

    def delete(self,node):
        try:
            if node.lchild and not node.rchild:
                pre=self.get_pre(node.key)
                value=pre.key
                self.delete(pre)
                node.key=value
            elif node.rchild and not node.lchild:
                if node.is_left_child():
                    node.rchild.parent=node.parent
                    node.parent.lchild=node.rchild
                else:
                    node.rchild.parent=node.parent
                    node.parent.rchild=node.rchild
            elif node.lchild and node.rchild:
                successor=self.get_successor(node.key)
                value=successor.key
                self.delete(successor)
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

    def tree_rotate_ll(self,node):
        if not node.parent:
            self.root=node.lchild
            node.lchild.parent=None
        else:
            node.lchild.parent=node.parent
            if node.is_left_child():
                node.parent.lchild=node.lchild
            else:
                node.parent.rchild=node.lchild
        temp_node=node.lchild.rchild
        node.lchild.rchild=node
        node.parent=node.lchild
        if temp_node:
            temp_node.parent=node
        node.lchild=temp_node

    def tree_rotate_rr(self,node):
        if not node.parent:
            self.root=node.rchild
            node.rchild.parent=None
        else:
            node.rchild.parent=node.parent
            if node.is_left_child():
                node.parent.lchild=node.rchild
            else:
                node.parent.rchild=node.rchild
        temp_node=node.rchild.lchild
        node.rchild.lchild=node
        node.parent=node.rchild
        if temp_node:
            temp_node.parent=node
        node.rchild=temp_node

    def tree_rotate_lr(self,node):
        node.lchild.rchild.parent=node
        temp_node=node.lchild.rchild.lchild
        node.lchild.rchild.lchild=node.lchild
        node.lchild=node.lchild.rchild
        node.lchild.lchild.rchild=None
        node.lchild.lchild.parent=node.lchild
        if temp_node:
            temp_node.parent=node.lchild.lchild
            node.lchild.lchild.rchild=temp_node
        self.tree_rotate_ll(node)

    def tree_rotate_rl(self,node):
        node.rchild.lchild.parent=node
        temp_node=node.rchild.lchild.rchild
        node.rchild.lchild.rchild=node.rchild
        node.rchild=node.rchild.lchild
        node.rchild.rchild.lchild=None
        node.rchild.rchild.parent=node.rchild
        if temp_node:
            temp_node.parent=node.rchild.rchild
            node.rchild.rchild.lchild=temp_node
        self.tree_rotate_rr(node)
    
    def check_imbanlance(self,node):
        result=self.find_imbanlance_node(node)
        if result:
            self.check_imbanlance_helper(result)
        else:
            pass

    def find_imbanlance_node(self,node):
        result= node
        while self.is_balance(result):
            if result.parent:
                result=result.parent
            else:
                result=None
                break
        return result

    def check_imbanlance_helper(self,node):
        if not self.is_balance(node):
            if self.get_bf(node)>1:                    #如果平衡因子大于1，那肯定是LL或者LR
                if self.get_node_h(node.lchild.lchild)>self.get_node_h  (node.lchild.rchild):               #左子树的左子树高度大于左子树的右子树，可以判定为LL
                    self.tree_rotate_ll(node)
                else:                               #小于则为LR
                    self.tree_rotate_lr(node)
            else:                                       #平衡因子小于1，那肯定是RR或者RL
                if self.get_node_h(node.rchild.rchild)>self.get_node_h(node.rchild.lchild):                #右子树的右子树高度大于右子树的左子树，可以判定为RR
                    self.tree_rotate_rr(node)
                else:                               #小于则为RL
                    self.tree_rotate_rl(node)
        else:
            pass

    
def test():
    bst=AVLTree()
    bst.insert(8)
    bst.insert(3)
    bst.insert(4)
    bst.insert(5)
    bst.insert(7)
    bst.insert(6)
    bst.insert(11)
    bst.insert(9)

  


    bst.insert(12)
    bst.insert(32)
    bst.insert(33)
    bst.insert(34)
    bst.insert(35)
    bst.insert(36)
    bst.insert(37)
    bst.insert(38)
    bst.insert(39)

    bst.remove(11)
    bst.remove(9)
    bst.remove(3)
    bst.remove(4)
    bst.remove(5)
    bst.remove(6)
    bst.remove(7)
    bst.remove(8)
    print bst.get_node_h(bst.find(37))

test()