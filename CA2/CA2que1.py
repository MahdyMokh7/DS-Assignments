import sys
import re


class Queue:
    def __init__(self):
        self.my_queue = []

    def getSize(self):
        return len(self.my_queue)

    def enqueue(self, value):
        self.my_queue.append(value)

    def dequeue(self):
        x = self.my_queue[0]
        self.my_queue = self.my_queue[1:]
        return x

    def isEmpty(self):
        return len(self.my_queue) == 0

    def getInOneLine(self):
        return ' '.join(self.my_queue)


class Stack:
    def __init__(self, size=10):
        self.my_stack = []
        self.size = size

    def isEmpty(self):
        return True if len(self.my_stack) == 0 else False

    def push(self, value):
        self.my_stack.append(value)

    def pop(self):
        return self.my_stack.pop()

    def put(self, value):
        self.my_stack.pop()
        self.my_stack.append(value)

    def peek(self):
        return self.my_stack[-1]

    def expand(self):
        self.size *= 2

    def getInOneLine(self):
        return ' '.join(self.my_stack)

    def getSize(self):
        return len(self.my_stack)
    
    def getCapacity(self):
        return self.size


class Node:
    def __init__(self, val):
        self.key = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def getList(self):
        node_x = self.head
        list_ = []
        while node_x is not None:
            list_.append(node_x.key)
            node_x = node_x.next
        return ' '.join(list_)

    def insertFront(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.head.next = None
        else:
            new_node.next = self.head
            self.head = new_node

    def insertEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.head.next = None
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def reverse(self):
        if self.head and self.head.next:
            cur = self.head.next
            prev = self.head
            while cur:
                nextt = cur.next

                cur.next = prev
                prev.prev = cur
                if prev == self.head:
                    prev.next = None

                # step forward
                prev = cur
                cur = nextt

            self.head = prev


class Runner:
    dsMap = {'stack': Stack, 'queue': Queue, 'linked_list': LinkedList}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, ]*)\)$')

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
        args = argsList.split(',') if argsList != '' else []

        method = getattr(self.items[itemName], funcName)
        result = method(*args)
        if result is not None:
            print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
