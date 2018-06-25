from sys import stdin
import time

class Node:
    def __init__(self, sum, key, parent, left, right):
        self.sum = sum
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return ("SUM: %s | KEY: %s  | PARENT: %s  | LEFT: %s  | RIGHT: %s "
        % (self.sum, self.key,
        (self.parent.key if self.parent != None else '-'),
        (self.left.key if self.left != None else '-'),
        (self.right.key if self.right != None else '-')))

class Tree:
    def __init__(self):
        self.root = None

    def update(self, key):
        if key == None:
            return
        key.sum = (key.key +
                    (key.left.sum if key.left != None else 0) +
                    (key.right.sum if key.right != None else 0))
        if key.left != None:
            key.left.parent = key
        if key.right != None:
            key.right.parent = key

    def small_rotation(self, key):
        parent = key.parent
        if parent == None:
            return
        grand_parent = parent.parent
        if parent.left == key:
            next = key.right
            key.right = parent
            parent.left = next
        elif parent.right == key:
            next = key.left
            key.left = parent
            parent.right = next
        self.update(parent)
        self.update(key)
        key.parent = grand_parent
        if grand_parent != None:
            if grand_parent.left == parent:
                grand_parent.left = key
            elif grand_parent.right == parent:
                grand_parent.right = key

    def big_rotation(self, key):
        parent = key.parent
        grand_parent = parent.parent
        if parent.left == key and grand_parent.left == parent:
            self.small_rotation(parent)
            self.small_rotation(key)
        elif parent.right == key and grand_parent.right == parent:
            self.small_rotation(parent)
            self.small_rotation(key)
        else:
            self.small_rotation(key)
            self.small_rotation(key)

    def splay(self, key):
        if key == None:
            return None
        while key.parent != None:
            if key.parent.parent == None:
                self.small_rotation(key)
                break
            self.big_rotation(key)
        return key

    def find(self, key, root):
        node = root
        last = root
        result = None
        while node != None:
            if node.key >= key and (result == None or node.key < result.key):
                result = node
            last = node
            if node.key == key:
                break
            elif node.key < key:
                node = node.right
            elif node.key > key:
                node = node.left
        self.root = self.splay(last)
        return result, self.root

    def split(self, key, root):
        result, self.root = self.find(key, root)
        if result == None:
            left, right = self.root, result
            return left, right
        right = self.splay(result)
        left = right.left
        right.left = None
        if left != None:
            left.parent = None
        self.update(left)
        self.update(right)
        return left, right

    def merge(self, left, right):
        if left == None:
            return right
        if right == None:
            return left
        while right.left != None:
            right = right.left
        self.root = self.splay(right)
        self.root.left = left
        self.update(self.root)
        return self.root

    def insert(self, key):
        left, right = self.split(key, self.root)
        new_node = None
        if right == None or right.key != key:
            new_node = Node(key, key, None, None, None)
        self.root = self.merge(self.merge(left, new_node), right)

    def delete(self, key):
        key, self.root = self.find(key, self.root)
        if key == None:
            return None
        self.root = self.merge(self.root.left, self.root.right)
        if self.root != None:
            self.root.parent = None

    def search(self, key, info=None):
        result, self.root = self.find(key, self.root)
        if result == None or int(result.key) != int(key):
            return None
        if info == None:
            return result.key
        elif info != None:
            return result

    def range_sum(self, fr, to):
        answer = 0
        left, middle = self.split(fr, self.root)
        middle, right = self.split(to + 1, middle)
        if middle == None:
            answer = 0
            self.root = self.merge(left, right)
        elif middle != None:
            answer = middle.sum
            self.root = self.merge(self.merge(left, middle), right)
        return answer

class SetRangeSum:
    def __init__(self):
        self.modulo = 1000000001
        self.last_sum_result = 0
        self.tree = Tree()

    def solve(self):
        n = int(stdin.readline())
        for i in range(n):
            line = stdin.readline().split()
            if line[0] == '+':
                x = int(line[1])
                self.tree.insert((x + self.last_sum_result) % self.modulo)
            elif line[0] == '-':
                x = int(line[1])
                self.tree.delete((x + self.last_sum_result) % self.modulo)
            elif line[0] == '?':
                x = int(line[1])
                print('Found' if self.tree.search((x + self.last_sum_result) % self.modulo)
                    else 'Not found')
            elif line[0] == 's':
                l = int(line[1])
                r = int(line[2])
                result = self.tree.range_sum((l + self.last_sum_result) % self.modulo,
                                            (r + self.last_sum_result) % self.modulo)
                print(result)
                self.last_sum_result = result % self.modulo

if __name__=="__main__":
    set = SetRangeSum()
    set.solve()
