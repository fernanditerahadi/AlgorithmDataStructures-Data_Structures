# python3
import sys
class DisjointSet:
    def __init__(self, n):
        self.rank = [0] + [0] * n
        self.parent = [0] + [x for x in range(1,n+1)]

    def Find(self, i):
        temp_parents = []
        while i != self.parent[i]:
            temp_parents += [self.parent[i]]
            i = self.parent[i]
        for j in temp_parents:
            self.parent[j] = i
        return i

    def Union(self, source, destination):
        source_root = self.Find(source)
        destination_root = self.Find(destination)
        if source_root == destination_root:
            return
        if self.rank[source_root] > self.rank[destination_root]:
            self.parent[destination_root] = source_root ; target = 'source'
        else:
            self.parent[source_root] = destination_root ; target = 'destination'
            if self.rank[source_root] == self.rank[destination_root]:
                self.rank[destination_root] = self.rank[destination_root] + 1
        return source_root, destination_root, target

    def Output(self):
        print('Parent :', self.parent, '\nRank   :', self.rank) ; return ''

class MergingTables:
    def read_data(self):
        self.n, self.m = map(int, sys.stdin.readline().split())
        self.table_rows = [0] + list(map(int, sys.stdin.readline().split()))
        self.max_rows = max(self.table_rows)

    def update(self, x, y):
        self.table_rows[x] += self.table_rows[y]
        self.table_rows[y] = 0
        if self.table_rows[x] > self.max_rows:
            self.max_rows = self.table_rows[x]

    def merge(self):
        tables = DisjointSet(self.n)
        for i in range(self.m):
            destination, source = map(int, sys.stdin.readline().split())
            try:
                source_root, destination_root, target  = tables.Union(source, destination)
                if target is 'destination':
                    self.update(destination_root, source_root)
                elif target is 'source':
                    self.update(source_root, destination_root)
            except:
                pass
            print(self.max_rows)

    def solve(self):
        self.read_data()
        self.merge()

if __name__ == "__main__":
    merge_table = MergingTables()
    merge_table.solve()
