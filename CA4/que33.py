import pdb


class Node:
    def __init__(self, name: int):
        self.name = name
        self.neighbors = []  # list nodes
        self.depth = 0
        self.color = 'white'
        self.f_time = 0
        self.d_time = 0
        self.leaves = set()
        self.is_leaf = False
        self.parent = 0

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def update_depth(self, depth):
        self.depth = depth

    def add_parent(self, p):
        self.parent = p


class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node: Node):
        self.nodes.append(node)

    def find_node(self, name):
        return self.nodes[name - 1]


clk = 0
def DFS(start_node: Node, parent_depth: int) -> set:
    global ans
    global clk
    start_node.color = 'gray'
    start_node.d_time = clk
    clk += 1
    start_node.depth = parent_depth + 1
    is_leaf = True
    for neighbor in start_node.neighbors:
        if neighbor.color == 'white':
            neighbor.parent = 12
            is_leaf = False
            neighbor.add_parent(start_node.name)
            start_node.leaves.update(DFS(neighbor, start_node.depth))

    start_node.color = 'black'
    if is_leaf:
        start_node.is_leaf = True
        clk += 1
        start_node.f_time = clk
        return {start_node.name, }
    else:
        start_node.is_leaf = False
        start_node.f_time = clk
        return start_node.leaves


def find_masir(node1: Node, node2: Node) -> list:  # from node1 to node2
    path = []
    path_reverse = []
    cur1 = node1
    cur2 = node2
    if node1.depth >= node2.depth:
        for i in range(node1.depth - node2.depth):
            path.append(cur1.name)
            cur1 = graph.find_node(cur1.parent)
        while cur1 != cur2:
            path.append(cur1.name)
            path_reverse.append(cur2.name)
            cur1 = graph.find_node(cur1.parent)
            cur2 = graph.find_node(cur2.parent)
        path.append(cur1.name)
        path_reverse.reverse()
        path.extend(path_reverse)
    elif node1.depth < node2.depth:
        for i in range(node2.depth - node1.depth):
            path_reverse.append(cur2.name)
            cur2 = graph.find_node(cur2.parent)
        while cur1 != cur2:
            path.append(cur1.name)
            path_reverse.append(cur2.name)
            cur1 = graph.find_node(cur1.parent)
            cur2 = graph.find_node(cur2.parent)
        path.append(cur1.name)
        path_reverse.reverse()
        path.extend(path_reverse)
    return path


if __name__ == '__main__':
    n = int(input())
    ans = []

    # pre-process
    graph = Graph()
    for i in range(n):
        new_node = Node(i + 1)
        graph.add_node(new_node)

    # getting the adjacency and updating the neighbors
    for i in range(n - 1):
        v, u = list(map(int, input().split()))
        v_node = graph.find_node(v)
        u_node = graph.find_node(u)

        # updating
        v_node.neighbors.append(u_node)
        u_node.neighbors.append(v_node)





    a = DFS(graph.find_node(1), -1)

    k = list(map(int, input().split()))



    ## print debug
    # for node in graph.nodes:
    #     print(node.name, node.parent)



    # main code
    path_ans = []

    path_ans.extend(find_masir(graph.find_node(1), graph.find_node(k[0])))
    for i in range(len(k) - 1):
        path_ans.pop()
        path_ans.extend(find_masir(graph.find_node(k[i]), graph.find_node(k[i + 1])))

    path_ans.pop()
    path_ans.extend(find_masir(graph.find_node(k[-1]), graph.find_node(1)))

    path_ans.pop()
    if len(path_ans) == 2*n - 2:
        print(*path_ans)
    else:
        print(-1)








