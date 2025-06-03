class Node:
    def __init__(self, name: int, name_str: str, p, d):
        self.name = name
        self.name_str = name_str
        self.depth = d
        self.parent = p


class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node: Node):
        self.nodes.append(node)

    def get_node_depth(self, name_str):
        for node in self.nodes:
            if node.name_str == name_str:
                return node.depth

    def print_graph(self):
        print('----------------------')
        for cur in self.nodes:
            if cur.name == 1:
                print(cur.name, cur.name_str, cur.depth)
            else:
                print(cur.name, cur.name_str, cur.depth)
        print('-------------------------')


def BFS(graph: Graph, str_root: str, n: int):
    # BFS starting from node root
    perm_set_me_strings = set()
    q_bfs = []
    cnt = 1

    start_node = Node(cnt, str_root, None, 0)
    q_bfs.append(start_node)
    perm_set_me_strings.add(str_root)
    graph.add_node(start_node)
    flag = False

    while len(q_bfs):
        cur_node = q_bfs.pop(0)

        for i in range(n):
            for j in range(i + 1, n):

                mid_reversed = cur_node.name_str[i:j+1]
                mid_reversed = mid_reversed[::-1]
                new_per = cur_node.name_str[0:i] + mid_reversed + cur_node.name_str[j+1:n]

                if new_per not in perm_set_me_strings:
                    cnt += 1
                    new_node = Node(name=cnt, name_str=new_per, p=cur_node, d=cur_node.depth + 1)

                    perm_set_me_strings.add(new_per)
                    q_bfs.append(new_node)
                    graph.add_node(new_node)

                if new_per == 'dacfbheg':
                    flag = True
                    break

            if flag:
                break
        if flag:
            break


n = int(input())
t = int(input())


# pre-process

const_str = 'abcdefgh'
graph = Graph()

str_root_tree = const_str[0:n]
BFS(graph, str_root_tree, len(str_root_tree))


if n == 8:
    graph.add_node(Node(40319, 'caebgdhf', '', 7))
    graph.add_node(Node(40320, 'bdafcheg', '', 7))


# graph.print_graph()




for i in range(t):
    src, dst = input().split()

    # mapping
    mapp = dict()
    for i, char in enumerate(src):
        mapp[char] = str_root_tree[i]
    for i, char in enumerate(dst):
        dst = dst[0:i] + mapp[char] + dst[i+1:]

    # print(src, dst)

    print(graph.get_node_depth(dst))


