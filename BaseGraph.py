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
        self.cc_count = 0             # 连通分量的数量
        self.cc_id = [0] * total               # 连通分量的id
        self.has_cycle = False         # 是否有环
        self.color = [False] * total
        self.is_two_color = True
        self.init_value(total)  # 初始化顶点

    def init_value(self, total):
        # 初始化邻接矩阵
        for x in range(total):
            self.adj.append([])     # 有没有更规范的写法？

    def addEdge(self, x, y):
        # 添加一条边
        elementx = self.adj[x]
        elementx.append(y)
        if not self.is_di:      # 如果是无向图，除了x——>y，还有y——>x也要添加进去
            elementy = self.adj[y]
            elementy.append(x)
        self.e += 1

    def adj(self, x):
        # 返回x指向的所有顶点
        return self.adj[x]

    def reverse(self):
        # 反转一个有向图，无向图会得到自身
        reverse_graph = BaseGraph(self.v, self.is_di)
        for x in range(self.v):
            for y in self.adj[x]:
                reverse_graph.addEdge(y, x)
        return reverse_graph

    def get_v_num(self):
        # 返回顶点的数量
        return self.v

    def get_e_num(self):
        # 返回边的数量
        return self.e

    def has_path_to(self, v):
        # 是否有到V的路径
        return self.marked[v]

    def path_to(self, v):
        # 到达V的路径
        if not self.marked[v]:
            return None
        else:
            temp = v
            path = [temp]
            while temp != self.start:
                temp = self.edgeTo[temp]
                path.append(temp)
            path.reverse()  # 翻转数组，即起点到终点的路径
            return path

    def dfs(self, x):
        # 深度优先搜索
        self.marked = [False] * self.v   # 初始所有的顶点都是未访问过的
        self.start = x
        self.dfs_helper(self.start)
        return self

    def dfs_helper(self, x):
        self.marked[x] = True
        self.cc_id[x] = self.cc_count
        for neighbour in self.adj[x]:
            if not self.marked[neighbour]:
                self.edgeTo[neighbour] = x
                self.dfs_helper(neighbour)
                self.color[neighbour] = self.color[x]
            else:
                if self.color[neighbour] == self.color[x]:
                    self.is_two_color = False
                self.has_cycle = True

    def bfs(self, x):
        # 广度优先搜索
        self.marked = [False] * self.v   # 初始所有的顶点都是未访问过的
        self.start = x
        self.bfs_helper(self.start)
        return self

    def bfs_helper(self, x):
        self.marked[x] = True
        queue = [x]
        while queue:
            v = queue.pop(0)
            for neighbour in self.adj[v]:
                if not self.marked[neighbour]:
                    self.marked[neighbour] = True
                    self.edgeTo[neighbour] = v
                    queue.append(neighbour)

    def cc(self):
        # 计算连通分量
        self.cc_count = 0
        self.marked = [False] * self.v   # 初始所有的顶点都是未访问过的
        for x in range(self.v):
            if not self.marked[x]:
                self.dfs_helper(x)
                self.cc_count += 1
        return self

    def connected(self, v, w):
        return self.cc_id[v] == self.cc_id[w]

    def get_cc_id(self, v):
        return self.cc_id[v]

    def get_cc_count(self):
        return self.cc_count

    def get_cc_sets(self):
        # 返回各个连通分量的集合
        cc_list = []
        for m in range(self.cc_count):
            cc_list.append([])
        for x in range(self.v):
            cc_list[self.cc_id[x]].append(x)
        return cc_list

    def has_cycles(self):
        # 是否有环
        return self.has_cycle

    def is_bipartite(self):
        # 是否是二分图
        return self.is_two_color


if __name__ == '__main__':
    a = BaseGraph(8, False)
    a.addEdge(0, 1)
    a.addEdge(0, 2)
    a.addEdge(1, 3)
    a.addEdge(1, 4)
    a.addEdge(1, 2)
    a.addEdge(2, 3)
    a.addEdge(2, 4)
    a.addEdge(3, 5)
    a.addEdge(4, 5)
    a.addEdge(1, 5)
    a.addEdge(1, 6)
    a.addEdge(4, 7)
    a.addEdge(7, 6)
    print a.dfs(0).path_to(5)
    print a.bfs(0).path_to(5)
    print a.cc().get_cc_sets()
    print a.has_cycles()
    print a.is_bipartite()
