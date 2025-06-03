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
        self.parent = None

    def add_neighbor(self, node):
        self.neighbors.append(node)

    def update_depth(self, depth):
        self.depth = depth


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
    depth_node.append((start_node.depth, start_node.name))
    for neighbor in start_node.neighbors:
        if neighbor.color == 'white':
            is_leaf = False
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


def DFS2(start_node: Node):
    global leaves_inp
    global ans

    start_node.color = 'gray'
    for neighbor in start_node.neighbors:
        if neighbor.color == 'white' and leaves_inp[0] in neighbor.leaves:
            print(start_node.name)
            ans.append(start_node.name)
            DFS2(neighbor)
            if start_node.is_leaf == False:
                ans.append(start_node.name)

    start_node.color = 'black'
    if start_node.is_leaf:
        leaves_inp.pop(0)
    else:
        pass
        # ans.append(start_node.name)


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

    leaves_inp = list(map(int, input().split()))

    depth_node = list()

    # pdb.set_trace()
    DFS(graph.find_node(1), -1)

    depth_node.sort(key=lambda x: x[0], reverse=True)

    # ## print debug
    # for node in graph.nodes:
    #     print(node.name, node.leaves, node.depth, node.is_leaf)

    for itr in depth_node:
        node_name = itr[1]
        node = graph.find_node(node_name)
        flag = 0
        for i_leaf in leaves_inp:
            if flag > 0 and flag < len(node.leaves):
                if i_leaf in node.leaves:
                    flag += 1
                else:
                    print(node_name)
                    print(-1)
                    exit()
            elif flag == len(node.leaves):
                break

            elif i_leaf in node.leaves:
                flag += 1

    # init
    for node in graph.nodes:
        node.color = 'white'


    ## print debug
    for node in graph.nodes:
        print(node.name, node.leaves, node.depth, node.is_leaf, node.color)

    pdb.set_trace()
    DFS2(graph.find_node(1))
    # ans.pop()
    # print(*ans)

