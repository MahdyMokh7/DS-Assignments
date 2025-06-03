import sys
import re
import math
from collections import Counter


INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'
INFINITY = 1e9


class MinHeap:
    class Node:
        def __init__(self, value):
            self.value = value

    def __init__(self):
        self.list_nodes = []

    def check_validation(self, index, mode):
        if mode == 'index':
            try:
                index = int(index)
            except Exception as e:
                raise Exception(INVALID_INDEX)
            else:
                if not 0 <= index < len(self.list_nodes):
                    raise Exception(OUT_OF_RANGE_INDEX)
            return int(index)
        elif mode == 'empty':
            if len(self.list_nodes) == 0:
                raise Exception(EMPTY)

    def bubble_up(self, index_initial):
        index_initial = self.check_validation(index_initial, 'index')
        value_initial_node = self.list_nodes[index_initial].value
        for index_itr, node_itr in enumerate(self.list_nodes):
            if node_itr.value >= value_initial_node:
                self.__swap_nodes(index_itr, index_initial)  # bubbled up
                # validate the min-heap using heapify for the produced incorrect node
                self.__heapify_for_one_node(index_initial)
                break

    def bubble_down(self, index_initial):
        index_initial = self.check_validation(index_initial, 'index')
        value_initial_node = self.list_nodes[index_initial].value
        for index_itr in range(len(self.list_nodes) - 1, index_initial, -1):
            node_itr = self.list_nodes[index_itr]
            if node_itr.value <= value_initial_node:
                self.__swap_nodes(index_itr, index_initial)  # bubbled up
                # validate the min-heap using heapify for the produced incorrect node
                self.__heapify_for_one_node(index_itr)
                break

    def heap_push(self, value):  # correct indexing starting from 0
        new_node = self.Node(int(value))
        self.list_nodes.append(new_node)
        index = len(self.list_nodes) - 1
        while index > 0:  # goes up until the min-heap gets valid
            index_parent = self.__find_parent(index)
            if self.list_nodes[index_parent].value > self.list_nodes[index].value:
                self.__swap_nodes(index, index_parent)
                index = index_parent
            else:
                break

    def heap_pop(self):  # correct indexing starting from 0
        self.check_validation(-1, 'empty')
        val_root = self.list_nodes[0].value
        self.list_nodes[0] = self.list_nodes[-1]
        self.list_nodes.pop()
        self.__heapify_for_one_node(0)
        return val_root

    def find_min_child(self, index):  # correct indexing starting from 0
        index = self.check_validation(index, 'index')
        if self.__find_left_child(index) == -1:
            raise Exception(OUT_OF_RANGE_INDEX)
        elif self.__find_right_child(index) == -1:
            return self.__find_left_child(index)
        else:
            if self.list_nodes[self.__find_left_child(index)].value <=\
                    self.list_nodes[self.__find_left_child(index)].value:
                return self.__find_left_child(index)
            else:
                return self.__find_right_child(index)

    def __in_obj_find_min_child(self, index):  # correct indexing starting from 0
        if self.__find_left_child(index) == -1:
            return -1
        elif self.__find_right_child(index) == -1:
            return self.__find_left_child(index)
        else:
            if self.list_nodes[self.__find_left_child(index)].value <=\
                    self.list_nodes[self.__find_right_child(index)].value:
                return self.__find_left_child(index)
            else:
                return self.__find_right_child(index)

    def heapify(self, *args):  # correct indexing starting from 0
        for val in args:
            self.heap_push(val)

    def __heapify_for_one_node(self, index):  # correct indexing starting from 0
        while not self.is_leaf(index):  # until it's not a leaf go down
            index_min_child = self.__in_obj_find_min_child(index)
            if index_min_child == -1:
                break
            if self.list_nodes[index_min_child].value >= self.list_nodes[index].value:
                break
            self.__swap_nodes(index_min_child, index)
            index = index_min_child

    def is_leaf(self, index):
        return True if index >= math.floor(len(self.list_nodes) / 2) else False

    def __swap_nodes(self, index1, index2):  # correct indexing starting from 0
        first_node = self.list_nodes[index1]
        self.list_nodes[index1] = self.list_nodes[index2]
        self.list_nodes[index2] = first_node

    def __find_parent(self, index):  # correct indexing starting from 0
        return math.ceil(index / 2) - 1

    def __find_left_child(self, index):  # correct indexing starting from 0
        return index*2+1 if index*2+1 < len(self.list_nodes) else -1

    def __find_right_child(self, index):  # correct indexing starting from 0
        return index*2+2 if index*2+2 < len(self.list_nodes) else -1

    def heap_print(self):
        print([node.value for node in self.list_nodes])


class HuffmanTree:
    class Node:
        def __init__(self, rep, letter, total_letters=1):
            self.rep = rep
            self.total_letters = total_letters
            self.letter = letter

    def __init__(self):
        self.letter_rep = {}
        self.letter_code = {}
        self.list_nodes = []

    def set_letters(self, *args):
        self.letter_rep = {arg: 0 for arg in args}
        self.letter_code = {arg: '' for arg in args}

    def set_repetitions(self, *args):
        i = 0
        for letter in self.letter_rep.keys():
            self.letter_rep[letter] = args[i]
            new_node = self.Node(rep=args[i], letter=letter)
            self.list_nodes.append(new_node)
            self.__sort_list(self.list_nodes, i)
            i += 1

    def build_huffman_tree(self):
        while len(self.list_nodes) > 1:
            last1 = self.list_nodes[-1]  # less reps
            last2 = self.list_nodes[-2]

            # last1
            for char in last1.letter:
                self.letter_code[char] = '0' + self.letter_code[char]
            # last2
            for char in last2.letter:
                self.letter_code[char] = '1' + self.letter_code[char]

            # updating the list nodes
            self.list_nodes.pop()
            self.list_nodes.pop()
            self.list_nodes.append(self.Node(last1.rep + last2.rep, last1.letter + last2.letter, last1.total_letters + last2.total_letters))
            self.__sort_list(self.list_nodes, len(self.list_nodes) - 1)

    def get_huffman_code_cost(self):
        cost = 0
        for letter in self.letter_code.keys():
            cost += len(self.letter_code[letter]) * self.letter_rep[letter]
        return cost

    def text_encoding(self, text):
        letters = list(Counter(list(text)).keys())
        reps = list(Counter(list(text)).values())
        self.set_letters(*letters)
        self.set_repetitions(*reps)
        self.build_huffman_tree()

    def __sort_list(self, l: list, index: int):  # Descending
        for j in range(index, 0, -1):
            if l[j - 1].rep < l[j].rep:
                # swap
                temp = l[j - 1]
                l[j - 1] = l[j]
                l[j] = temp
            elif l[j].rep == l[j - 1].rep:
                if l[j - 1].total_letters < l[j].total_letters:
                    # swap
                    temp = l[j - 1]
                    l[j - 1] = l[j]
                    l[j] = temp
                else:
                    break
            else:
                break

    def print_everything(self):
        for node in self.list_nodes:
            print(node.rep, node.total_letters, end='  |  ')
        print()
        print(self.letter_rep)
        print(self.letter_code)


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
                        break
                    else:
                        cur = cur.left_child
                else:  # go to right child
                    if cur.right_child is None:
                        new_node = self.Node(key, parent=cur, left_child=None, right_child=None)
                        cur.right_child = new_node
                        cur.leaf = False
                        break
                    else:
                        cur = cur.right_child
            self.list_nodes.append(new_node)

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


class Runner:
    dsMap = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

    def __init__(self, inputSrc):
        self.input = inputSrc
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            actionMethod = getattr(self, action, None)
            if actionMethod is None:
                return
            actionMethod(param)

    def make(self, params):
        itemType, itemName = params.split()
        self.items[itemName] = self.dsMap[itemType]()

    def call(self, params):
        regexRes = self.callRegex.match(params)
        itemName, funcName, argsList = regexRes.groups()

        args = [x.strip() for x in argsList.split(',')] if argsList != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[itemName], funcName)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
