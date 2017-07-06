#!/usr/bin/python
# -*- coding: UTF-8 -*-

from avltree import Node
from avltree import AVLTree
from rbtree import RNode
from rbtree import RedBlackTree
import random
import time

RED=True
BLACK=False
num=3000

class RBNode(object):
    def __init__(self,k,v,c=RED,l=None,r=None):
        self.lchild=l
        self.rchild=r
        self.key=k
        self.color=c
        self.value=v

class Red_black_tree(object):
    def __init__(self):
        self.root=None
        self.node_size=0

    def is_red(self,node):
        if node:
            return node.color
        else:
            return False

    def put(self,k,v):
        node=self.root
        self.root=self.insert(node,k,v)
        self.root.color=BLACK

    def get(self,k):
        return self.search(self.root,k)

    def insert(self,node,k,v):
        if not node:
            return RBNode(k,v)

        if k==node.key:
            node.value=v
        elif k<node.key:
            node.lchild=self.insert(node.lchild,k,v)
        else:
            node.rchild=self.insert(node.rchild,k,v)
        
        if(self.is_red(node.rchild)):
            node=self.rotateLeft(node)

        if(self.is_red(node.lchild) and self.is_red(node.lchild.lchild)):
            node=self.rotateRight(node)
        
        
        if(self.is_red(node.lchild) and self.is_red(node.rchild)):
            self.colorFlip(node)

        return node

    def search(self,node,x):
        current_node=node
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
        if result:
            return result.value
        else:
            return None

    def rotateLeft(self,h):
        node=h.rchild
        h.rchild=node.lchild
        node.lchild=h
        node.color=node.lchild.color
        node.lchild.color=RED
        return node

    def rotateRight(self,h):
        node=h.lchild
        h.lchild=node.rchild
        node.rchild=h
        node.color=node.rchild.color
        node.rchild.color=RED
        return node

    def colorFlip(self,h):
        h.color= not h.color
        h.lchild.color=not h.lchild.color
        h.rchild.color=not h.rchild.color
        return h
    
    def fixUp(self,h):
        if self.is_red(h.rchild):
            h=self.rotateLeft(h)

        if self.is_red(h.lchild) and self.is_red(h.lchild.lchild):
            h=self.rotateRight(h)

        if self.is_red(h.lchild) and self.is_red(h.rchild):
            h=self.colorFlip(h)
        
        return h

    def moveRedRight(self,h):
        self.colorFlip(h)
        if self.is_red(h.lchild.lchild):
            h=self.rotateRight(h)
            self.colorFlip(h)
        return h

    def moveRedLeft(self,h):
        self.colorFlip(h)
        if self.is_red(h.rchild.lchild):
            h.rchild=self.rotateRight(h.rchild)
            h=self.rotateLeft(h)
            self.colorFlip(h)
        return h

    def deleteMin(self,h):
        if not h.lchild:           ##为何，因为不可能出现黑节点在右而左节点为空的情况。而在LLRBT里，红节点一直在左
            return None

        if self.is_red(h.lchild) and self.is_red(h.lchild.lchild):
            h=self.moveRedLeft(h)

        h.lchild=self.deleteMin(h.lchild)
        return self.fixUp(h)

    def remove(self,k):
        self.root = self.delete(self.root, k)
        if self.root:
            self.root.color = BLACK

    def delete(self,h,k):
        if k<h.key:
            if(not self.is_red(h.lchild) and not self.is_red(h.lchild.lchild)):
                h=self.moveRedLeft(h)
            h.lchild=self.delete(h.lchild,k)
        else:
            if self.is_red(h.lchild):
                h=self.rotateRight(h)
            if k==h.key and h.rchild==None:
                return None
            if not self.is_red(h.rchild) and not self.is_red(h.rchild.lchild):
                h=self.moveRedRight(h)
            if k==h.key:
                h.key=self.min(h.rchild)
                h.value=self.search(h.rchild,h.key)
                h.rchild=self.deleteMin(h.rchild)
            else:
                h.rchild=self.delete(h.rchild,k)
        return self.fixUp(h)

    def min(self):
        if (self.root == None): 
            return None
        else:              
            return min(self.root)

    def min(self, x):
        if (x.lchild == None): 
            return x.key
        else:
            return self.min(x.lchild)

def drawSnake(rad, angle, len, neckrad):
    for _ in range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.forward(rad/2) # 直线前进
    turtle.circle(neckrad, 180)
    turtle.forward(rad/4)
    turtle.done()

def draw_circle():
    turtle.circle()


def cal_func_time(string,func):
    # print lists
    start = time.clock()
    func()
    end = time.clock()
    print string+str(end-start)

def avl_insert(string):
    start = time.clock()
    avl= AVLTree()
    for i in range(num):
        avl.insert(i)
    end = time.clock()
    print string+str(end-start)

def avl_remove(string):
    avl= AVLTree()
    for i in range(num):
        avl.insert(i)
    start = time.clock()
    for i in range(num):
        avl.remove(i)
    end = time.clock()
    print string+str(end-start)

def avl_search(string):
    avl= AVLTree()
    for i in range(num):
        avl.insert(i)
    start = time.clock()
    for i in range(num):
        avl.find(i)
    end = time.clock()
    print string+str(end-start)

def llrbt_insert(string):
    start = time.clock()
    rbt= Red_black_tree()
    for i in range(num):
        rbt.put(i,i)
    end = time.clock()
    print string+str(end-start)

def llrbt_remove(string):
    rbt= Red_black_tree()
    for i in range(num):
        rbt.put(i,i)
    start = time.clock()
    for i in range(num):
        rbt.remove(i)
    end = time.clock()
    print string+str(end-start)

def llrbt_search(string):
    rbt= Red_black_tree()
    for i in range(num):
        rbt.put(i,i)
    start = time.clock()
    for i in range(num):
        rbt.get(i)
    end = time.clock()
    print string+str(end-start)

def rbt_insert(string):
    start = time.clock()
    rbt= RedBlackTree()
    for i in range(num):
        rbt.insert(i)
    end = time.clock()
    print string+str(end-start)

def rbt_remove(string):
    rbt= RedBlackTree()
    for i in range(num):
        rbt.add(i)
    start = time.clock()
    for i in range(num):
        rbt.remove(i)
    end = time.clock()
    print string+str(end-start)

def rbt_search(string):
    rbt= RedBlackTree()
    for i in range(num):
        rbt.add(i)
    start = time.clock()
    for i in range(num):
        rbt.find_node(i)
    end = time.clock()
    print string+str(end-start)


def test():
    # rbt=Red_black_tree()
    # rbt.put(3,2)
    # rbt.put(2,4)
    # rbt.put(1,55)
    # rbt.put(4,234)
    # rbt.put(5,24)
    # rbt.put(12,3432)
    # rbt.put(21,55)
    # rbt.put(24,234)
    # rbt.put(25,24)
    # rbt.put(122,3432)
    # rbt.put(121,33)
    # rbt.put(31,55)
    # rbt.put(43,234)
    # rbt.put(53,24)
    # rbt.put(312,3432)
    # rbt.put(311,33)
    # rbt.put(25,24)
    # rbt.put(122,3432)
    # rbt.put(1221,33)
    # rbt.put(321,55)
    # rbt.put(423,234)
    # rbt.put(533,24)
    # rbt.put(3412,3432)
    # rbt.put(3111,33)
    # rbt.put(13,234)
    # rbt.put(23,24)
    # rbt.put(33212,3432)
    # rbt.put(3311,33)
    # rbt.put(245,24)
    # rbt.put(143222,3432)
    # rbt.put(1224321,33)
    # rbt.put(3211,55)
    # rbt.put(43223,234)
    # rbt.put(53323,24)
    # rbt.put(34112,3432)
    # rbt.put(311121,33)

    # rbt.remove(31)
    # rbt.remove(12)
    # print rbt.get(3)
    # print rbt.get(4)
    # print rbt.get(12)


    # bst=AVLTree()
    # bst.insert(8)
    # bst.insert(3)
    # bst.insert(4)
    # bst.insert(5)
    # bst.insert(7)
    # bst.insert(6)
    # bst.insert(11)
    # bst.insert(9)

  


    # bst.insert(12)
    # bst.insert(32)
    # bst.insert(33)
    # bst.insert(34)
    # bst.insert(35)
    # bst.insert(36)
    # bst.insert(37)
    # bst.insert(38)
    # bst.insert(39)

    avl_insert("avl插入     ")
    avl_remove("avl删除     ")
    avl_search("avl查询     ")

    llrbt_insert("llrbt插入     ")
    llrbt_remove("llrbt删除     ")
    llrbt_search("llrbt查询     ")

    # turtle.screensize()
    # turtle.setup(width=800, height=800, startx=100, starty=100)
    # drawSnake(70,80,2,15)


test()


