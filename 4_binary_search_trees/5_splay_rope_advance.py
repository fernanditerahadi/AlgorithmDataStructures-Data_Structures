#Uses Python3
import sys
class Node:
    def __init__(self, size, key, parent, left, right):
        self.size = size
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return ("SIZE: %s | KEY: %s  | PARENT: %s  | LEFT: %s  | RIGHT: %s "
        % (self.size, self.key,
        (self.parent.key if self.parent != None else '-'),
        (self.left.key if self.left != None else '-'),
        (self.right.key if self.right != None else '-')))

class Tree:
    def __init__(self):
        self.root = None

    def update(self, key):
        if key == None:
            return
        key.size = (1 +
                    ((key.left.size if key.left != None else 0) +
                    (key.right.size if key.right != None else 0)))
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
        else:
            next = key.left
            key.left = parent
            parent.right = next
        self.update(parent)
        self.update(key)
        key.parent = grand_parent
        if grand_parent != None:
            if grand_parent.left == parent:
                grand_parent.left = key
            else:
                grand_parent.right = key

    def big_rotation(self, key):
        if key.parent.left == key and key.parent.parent.left == key.parent:
            self.small_rotation(key.parent)
            self.small_rotation(key)
        elif key.parent.right == key and key.parent.parent.right == key.parent:
            self.small_rotation(key.parent)
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
        while node != None:
            if node.left != None:
                size = node.left.size
            else:
                size = 0
            if key == (size+1):
                break
            elif key < (size+1):
                node = node.left
            elif key > (size+1):
                if node.right is None:
                    break
                node = node.right
                key = key - size - 1
        self.root = self.splay(node)
        return node, self.root

    def split(self, key, root):
        result, self.root = self.find(key, root)
        if result == None:
            return self.root, None
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
        right = self.splay(right)
        right.left = left
        self.update(right)
        return right

    def in_order(self, index):
        result = ""
        current = index
        while current != None:
            if current.left == None:
                result += str(current.key)
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right != None and predecessor.right != current:
                    predecessor = predecessor.right
                if predecessor.right == None:
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    result += str(current.key)
                    current = current.right
        return result

class Rope:
    def __init__(self, strings):
        self.rope = Tree()
        for s in strings:
            self.rope.root = self.rope.merge(self.rope.root, Node(1, s, None, None, None))
        self.rope.root = self.rope.merge(self.rope.root, Node(0, '', None, None, None))

    def process(self, i, j ,k):
        left, right = self.rope.split(i+1, self.rope.root)
        middle, right = self.rope.split(j+1-i+1, right)
        left, right = self.rope.split(k+1, self.rope.merge(left, right),)
        self.rope.root = self.rope.merge(self.rope.merge(left, middle), right)

    def print_result(self):
        return self.rope.in_order(self.rope.root).strip()

class SplayRope:
    def __init__(self):
        self.strings = sys.stdin.readline().strip()
        self.splay_rope = Rope(self.strings)
        self.query = int(sys.stdin.readline())

    def start(self):
        for q in range(self.query):
            i, j, k = map(int, sys.stdin.readline().strip().split())
            self.splay_rope.process(i, j, k)
            print(self.splay_rope.print_result())

if __name__=="__main__":
    splay_rope = SplayRope()
    splay_rope.start()
