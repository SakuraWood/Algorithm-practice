class Package(object):
    def __init__(self):
        self.capacity=20
        self.value=0
        self.weight=0
        self.nodes={}

    def get_value(self):
        return self.value

    def get_weight(self):
        return self.weight

    def get_rest(self):
        return self.capacity-self.weight

    def set_capacity(self,c):
        self.capacity=c

    def add_node(self,k,v):
        self.nodes[k]=v
    
    def remove_node(self,k):
        del self.nodes[k]

def func():
    pack=Package()
    


func()