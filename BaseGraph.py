from BiMap import BiMap


class BaseGraph(object):
    def __init__(self, total, isDirected):
        self.adj = []      # 邻接表
        self.is_di = isDirected  # 是否是有向图
        self.v = total              # 顶点个数
        self.e = 0              # 边的个数
        self.marked = [False] * total   # 初始所有的顶点都是未访问过的
        self.edgeTo = [0] * total  # 从起点到一个顶点在已知路径上的最后一个顶点
        self.start = 0             # 默认搜索起点为0
        self.init_value(total)  # 初始化顶点

    def init_value(self, total):
        for x in range(total):
            self.adj.append([])

    def addEdge(self, x, y):
        elementx = self.adj[x]
        elementx.append(y)
        if not self.is_di:
            elementy = self.adj[y]
            elementy.append(x)
        self.e += 1

    def adj(self, x):  # 返回x指向的所有顶点
        return self.adj[x]

    def get_v_num(self):
        return self.v

    def get_e_num(self):
        return self.e

    def has_path_to(self, v):
        return self.marked[v]

    def path_to(self, v):
        if not self.marked[v]:
            return None
        else:
            temp = v
            path = [temp]
            while temp != self.start:
                temp = self.edgeTo[temp]
                path.append(temp)
            path.append(self.start)
            return path.reverse()

    def dfs(self, x):
        self.start = x
        self.dfs_helper(self.start)
        return self

    def dfs_helper(self, x):
        self.marked[x] = True
        for neighbour in self.adj[x]:
            if not self.marked[neighbour]:
                self.edgeTo[neighbour] = x
                self.dfs_helper(neighbour)

    # def bfs(self, x):


if __name__ == '__main__':
    a = BaseGraph(8, True)
    a.addEdge(0, 2)
    a.addEdge(0, 1)
    a.addEdge(1, 3)
    a.addEdge(1, 4)
    a.addEdge(1, 2)
    a.addEdge(2, 3)
    a.addEdge(2, 4)
    a.addEdge(4, 5)
    a.addEdge(1, 5)
    a.addEdge(1, 6)
    a.addEdge(1, 7)
    a.addEdge(2, 7)
    a.addEdge(3, 7)
    a.addEdge(6, 7)
    print a.dfs(0).path_to(6)
