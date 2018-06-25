# python3
import sys, multiprocessing, time
sys.setrecursionlimit(10**6) # max depth of recursion

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = []
        self.left = []
        self.right = []
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key.append(a)
            self.left.append(b)
            self.right.append(c)

    def read_data(self):
        try:
            filehandle = open(r'C:\Users\User\Downloads\Week 5\Programming-Assignment-4\tree_orders\tests\21').read() #Change to your directory
        except:
            print('File not found')
            input()
        pos = filehandle.find('\n')
        self.n = int(filehandle[:pos])
        self.key = []
        self.left = []
        self.right = []
        for node in filehandle[pos:].strip().split('\n'):
            self.key.append(int(node.split()[0]))
            self.left.append(int(node.split()[1]))
            self.right.append(int(node.split()[2]))


    def in_order(self, index):
        result = []
        current = index
        while current != -1:
            if self.left[current] == -1:
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
                    result.append(self.key[current])
                    current = self.right[current]
        print(" ".join(str(x) for x in result))

    def pre_order(self, index):
        result = []
        current = index
        while current != -1:
            if self.left[current] == -1:
                result.append(self.key[current])
                current = self.right[current]
            else:
                predecessor = self.left[current] #1
                while self.right[predecessor] != -1 and self.right[predecessor] != current:
                    predecessor = self.right[predecessor] #4
                if self.right[predecessor] != current:
                    result.append(self.key[current])
                    self.right[predecessor] = current
                    current = self.left[current]
                else:
                    self.right[predecessor] = -1
                    current = self.right[current]
        print(" ".join(str(x) for x in result))

    def post_order(self, index):
        result = []
        self.key.append(0)
        self.left.append(0)
        self.right.append(-1)
        current = len(self.key)-1
        while current != -1:
            if self.left[current] == -1:
                current = self.right[current]
            else:
                predecessor = self.left[current] #1
                while self.right[predecessor] != -1 and self.right[predecessor] != current:
                    predecessor = self.right[predecessor]
                if self.right[predecessor] == -1:
                    self.right[predecessor] = current
                    current = self.left[current]
                else:
                    result.extend(self.trace_back(self.left[current],predecessor))
                    self.right[predecessor] = -1
                    current = self.right[current]
        print(" ".join(str(x) for x in result))

    def trace_back(self, node, parent):
        result = []
        current = node
        while current != parent:
            result.append(self.key[current])
            current = self.right[current]
        result.append(self.key[parent])
        result.reverse()
        return result

if __name__ =="__main__":
    tree = TreeOrders()
    #tree.read()
    tree.read_data()
    a = multiprocessing.Process(target=tree.in_order, args=(0,))
    b = multiprocessing.Process(target=tree.pre_order, args=(0,))
    c = multiprocessing.Process(target=tree.post_order, args=(0,))
    a.start()
    b.start()
    c.start()
    a.join()
    b.join()
    c.join()
