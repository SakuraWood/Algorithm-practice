class Map:
    def __init__(self):
        self.items=[]

    
    def put(self,k,v):
        self.items.append((k,v))
    

    def get(self,k):
        for key,value in self.items:
            if(k==key):
                return value
        raise "keyError"


class Map2:
    def __init__(self):
        self.items=[None]*100
    
    def hash(self,a):
        return a*1+0
    
    def put(self,k,v):
        self.items[self.hash(k)]=v

    def get(self,k):
        hashcode=self.hash(k)
        return self.items[hashcode]

class Map3:
    def __init__(self):
        self.hash_table=[[None,None]for i in range(11)]
    
    def hash(self,k,i):
        h_value=(k+i)%11
        if self.hash_table[h_value][0]==k:
            return h_value
        if self.hash_table[h_value][0]!=None:
            i+=1
            h_value=self.hash(k,i)
        return h_value
 
    def put(self,k,v):
        hash_v=self.hash(k,0)
        self.hash_table[hash_v][0]=k
        self.hash_table[hash_v][1]=v

    def get(self,k):
        hash_v=self.hash(k,0)
        return self.hash_table[hash_v][1]

class Map4:
    def __init__(self):
        self.capacity=11
        self.hash_table=[[None,None]for i in range(self.capacity)]# 每个元素是一个子数组，存放key和value，为什么要记住key？resize和get的时候有用
        self.num=0
        self.load_factor=0.75
    
    def hash(self,k,i):
        h_value=(k+i)%self.capacity
        if self.hash_table[h_value][0]==k:
            return h_value
        if self.hash_table[h_value][0]!=None:
            i+=1
            h_value=self.hash(k,i)
        return h_value

    def resize(self):
        self.capacity=self.num*2 #扩容到原有元素的两倍
        temp=self.hash_table[:]
        self.hash_table=[[None,None]for i in range(self.capacity)] 
        for i in temp:
            if(i[0]!=None):  #把原来已有的元素存入
                hash_v=self.hash(i[0],0)
                self.hash_table[hash_v][0]=i[0]
                self.hash_table[hash_v][1]=i[1]
 
    def put(self,k,v):
        hash_v=self.hash(k,0)
        self.hash_table[hash_v][0]=k
        self.hash_table[hash_v][1]=v
        self.num+=1
        if(self.num/len(self.hash_table)>self.load_factor):# 如果比例大于载荷因子
            self.resize()

    def get(self,k):
        hash_v=self.hash(k,0)
        return self.hash_table[hash_v][1]
    

def test():
    map=Map()
    map.put(3,4)
    print map.get(3)

    map1=Map2()
    map1.put(0,5)
    print map1.get(0)

    map2=Map3()
    map2.put(1,0)
    map2.put(2,12)
    map2.put(3,22)
    map2.put(4,23)
    map2.put(5,24)
    map2.put(6,25)
    map2.put(7,26)
    map2.put(8,27)

    print map2.get(3)

    map3=Map4()
    map3.put(1,0)
    map3.put(2,12)
    map3.put(3,22)
    map3.put(4,23)
    map3.put(5,24)
    map3.put(6,25)
    map3.put(7,26)
    map3.put(8,27)
    map3.put(12,12)
    map3.put(13,22)
    map3.put(14,23)
    map3.put(15,24)
    map3.put(16,25)
    map3.put(17,26)
    map3.put(18,27)

    print map3.get(4)
    

test()