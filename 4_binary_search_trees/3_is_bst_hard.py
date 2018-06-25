#!/usr/bin/python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class Tree:
    def read(self):
        self.nodes = int(sys.stdin.readline().strip())
        self.key = []
        self.left = []
        self.right = []
        for i in range(self.nodes):
            [a, b, c] = map(int, sys.stdin.readline().strip().split())
            self.key.append(a)
            self.left.append(b)
            self.right.append(c)

    def IsBinarySearchTree(self, index):
        result = []
        current = index
        while current != -1:
            if self.nodes == 0:
                return "CORRECT"
            elif self.left[current] == -1:
                if len(result) > 0 and result[-1] > self.key[current]:
                    return "INCORRECT"
                else:
                    result.append(self.key[current])
                    current = self.right[current]
            else:
                predecessor = self.left[current]
                while self.right[predecessor] != -1 and self.right[predecessor] != current:
                    predecessor = self.right[predecessor]
                if self.right[predecessor] == -1:
                    self.right[predecessor] = current
                    current = self.left[current]
                else:
                    self.right[predecessor] = -1
                    if len(result) > 0 and result[-1] >= self.key[current]:
                        return "INCORRECT"
                    else:
                        result.append(self.key[current])
                        current = self.right[current]
        return "CORRECT"

if __name__ == "__main__":
    check_tree = Tree()
    check_tree.read()
    print(check_tree.IsBinarySearchTree(0))
