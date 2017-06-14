class Graph:
    def __init__(self,maps,edgeNum=0):
        self.map=maps
        self.nodeNum=len(maps)
        self.edgeNum=edgeNum
    
    def getNodeNum(self):
        return self.nodeNum

    def getEdgeNum(self):
        self.edgeNum=0
        for i in range(self.nodeNum):
            for j in range(self.nodeNum-i):
                if self.map[i][j+i]==1:
                    self.edgeNum+=1
        return self.edgeNum

    def insertNode(self):
        for i in range(self.nodeNum):
            self.map[i].append(0)
        self.nodeNum+=1
        ls=[0]*self.nodeNum
        self.map.append(ls)

    def deleteNode(self,x):
        for i in range(self.nodeNum):
            if self.map[i][x]==1:
                self.map[i][x]=0
                self.edgeNum-=1
            if self.map[x][i]==1:
                self.map[x][i]=0
                self.edgeNum-=1

    def addEdge(self,x,y):
        if x<y:
            if self.map[x][y]==0:
                self.map[x][y]=1
                self.edgeNum+=1
        else:
            if self.map[y][x]==0:
                self.map[y][x]=1
                self.edgeNum+=1


    def removeEdge(self,x,y):
        if self.map[x][y]==1:
            self.map[x][y]=0
            self.edgeNum-=1

    def BFSearch(self):
        visited=[0]*self.nodeNum
        queue=[]
        def bfs(self,i):
            print i
            
            if(visited[i]==0):
                visited[i]=1
                for j in range(self.nodeNum):
                    if(self.map[i][j]==1 and visited[j]==0):
                        queue.append(j)
                for k in queue:
                    if(visited[k]==0):
                        bfs(self,k)
                del queue[:]
                
        for i in range(self.nodeNum):
            if(visited[i]==0):
                bfs(self,i)

    
    def DFSearch(self):
        visited=[0]*self.nodeNum
        def dfs(self,i):
           print i
           if(visited[i]==0):
               visited[i]=1
               for j in range(self.nodeNum-i):
                    if(self.map[i][j+i]==1 and visited[j+i]==0):
                        dfs(self,j+i)
        for i in range(self.nodeNum):
            if(visited[i]==0):
                dfs(self,i)

 


def test():
    maps=[[-1,1,0],
    [0,-1,1],
    [0,0,-1]]
    G=Graph(maps)
    print G.getNodeNum()
    G.insertNode()
    G.insertNode()
    G.insertNode()
    print G.getNodeNum()
    
    print G.getEdgeNum()
    G.addEdge(1,4)
    print G.getEdgeNum()
    G.addEdge(4,1)

    G.addEdge(4,3)
    G.addEdge(2,5)
    G.addEdge(4,5)
    G.addEdge(3,5)
    print G.getEdgeNum()
    
    G.DFSearch()
    G.BFSearch()
test()