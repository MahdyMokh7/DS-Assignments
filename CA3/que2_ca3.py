INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'
INFINITY = 1e9


class Bst:
    class Node:
        def __init__(self, value, parent=None, left_child=None, right_child=None, special_name=''):
            self.value = value
            self.parent = parent
            self.right_child = right_child
            self.left_child = left_child
            self.leaf = True
            self.special_name = special_name

    def __init__(self):
        self.nil = self.Node(value=INFINITY, parent=None, left_child=None, right_child=None, special_name='nil')
        self.list_nodes = []
        self.in_order_list_nodes = []
        self.parents = []

    def __initialize_root(self, node):
        self.root = node

    def insert(self, key):
        if len(self.list_nodes) == 0:
            root_node = self.Node(key)
            self.__initialize_root(root_node)
            self.list_nodes.append(root_node)
        else:
            cur = self.root
            while True:  # O(lg(h))
                if cur.value > key:  # go to left child
                    if cur.left_child is None:
                        new_node = self.Node(key, parent=cur, left_child=None, right_child=None)
                        cur.left_child = new_node
                        cur.leaf = False
                        self.parents.append(cur.value)
                        break
                    else:
                        cur = cur.left_child
                else:  # go to right child
                    if cur.right_child is None:
                        new_node = self.Node(key, parent=cur, left_child=None, right_child=None)
                        cur.right_child = new_node
                        cur.leaf = False
                        self.parents.append(cur.value)
                        break
                    else:
                        cur = cur.right_child
            self.list_nodes.append(new_node)

    def find_ancestor(self, index1, index2):
        cur1 = self.list_nodes[index1]
        cur2 = self.list_nodes[index2]
        depth_cur1 = self.__find_depth(cur1)
        depth_cur2 = self.__find_depth(cur2)

        if depth_cur1 > depth_cur2:
            for _ in range(depth_cur1 - depth_cur2):
                cur1 = cur1.parent
            while cur1 != cur2:
                cur1 = cur1.parent
                cur2 = cur2.parent
            return self.list_nodes.index(cur1) + 1
        else:
            for _ in range(depth_cur2 - depth_cur1):
                cur2 = cur2.parent
            while cur1 != cur2:
                cur1 = cur1.parent
                cur2 = cur2.parent
            return self.list_nodes.index(cur2) + 1

    def __find_depth(self, node: Node):
        depth = 0
        while node is not self.root:
            node = node.parent
            depth += 1
        return depth

    def search_node(self, key):
        cur = self.root
        while True:  # O(lg(h))
            if cur is None:
                return None
            if cur.value == key:
                return cur
            elif cur.value > key:  # go to left child
                cur = cur.left_child
            else:  # go to right child
                cur = cur.right_child

    def value_parent(self, key):
        # return self.search_node(key).parent.value
        return self.parents

    def inorder(self):
        self.in_order_list_nodes = []
        self.__in_order_internal(self.root)
        # return self.in_order_list_nodes

    def __in_order_internal(self, node: Node):
        if node is None:
            return
        self.__in_order_internal(node.left_child)
        self.in_order_list_nodes.append(node.value)
        print(node.value, end=' ')
        self.__in_order_internal(node.right_child)


def main():
    n = int(input())
    list_nums = list(map(int, input().split()))
    index_a, index_b = list(map(int, input().split()))

    tree = Bst()

    # print parents
    list_parents = []
    for i, num in enumerate(list_nums):
        tree.insert(num)
        if i > 0:
            pass
            # list_parents.append(tree.value_parent(num))
    print(' '.join(map(str, tree.parents)))

    # print ancestor
    print(tree.find_ancestor(index_a - 1, index_b - 1))


if __name__ == "__main__":
    main()

