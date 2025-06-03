import queue


class Node:
    def __init__(self, name: int):
        self.name = name
        self.neighbors = []  # list nodes
        self.depth = 0
        self.color = 'white'

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


if __name__ == '__main__':
    n, m = input().split()
    n = int(n)
    m = int(m)

    # pre-process
    graph = Graph()
    for i in range(n):
        new_node = Node(i + 1)
        graph.add_node(new_node)

    # getting the adjacency and updating the neighbors
    for i in range(m):
        v, u = list(map(int, input().split()))
        v_node = graph.find_node(v)
        u_node = graph.find_node(u)

        # updating
        v_node.neighbors.append(u_node)
        u_node.neighbors.append(v_node)

    # iterating over all nodes
    for k in range(n):
        # BFS starting from node 1
        first_node = graph.find_node(k + 1)
        if first_node.color == 'white':
            q_bfs = queue.Queue()
            q_bfs.put(first_node)
            while not q_bfs.empty():
                cur_node = q_bfs.get()
                for node_neighbor in cur_node.neighbors:
                    if node_neighbor.color == 'white':
                        q_bfs.put(node_neighbor)
                        node_neighbor.depth = cur_node.depth + 1
                        node_neighbor.color = 'gray'

                first_node.color = 'black'

    # iterate over all the nodes and separate the 2 teams by their depths mod2
    team1 = []
    for i in range(n):
        node = graph.find_node(i + 1)
        if node.depth % 2 == 0:
            team1.append(str(node.name))

    print(len(team1))
    print(' '.join(team1))



