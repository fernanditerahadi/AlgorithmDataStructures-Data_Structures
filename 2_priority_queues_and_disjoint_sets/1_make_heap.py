# python3
class HeapBuilder:
    def __init__(self):
        self._swaps = []
        self._data = [0]

    def ReadData(self):
        n = int(input())
        self._data += [int(s) for s in input().split()]
        assert n + 1 == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def GenerateSwaps(self):
        n = len(self._data)-1
        self.BuildHeap(self._data, n)

    def SiftDown(self, i, n):
        minIndex = i
        left = 2*i
        right = 2*i+1
        if left <= n and self._data[left] < self._data[minIndex]:
            minIndex = left
        if right <= n and self._data[right] < self._data[minIndex]:
            minIndex = right
        if i != minIndex:
            self._swaps += [(i-1, minIndex-1)]
            self._data[i], self._data[minIndex] = self._data[minIndex], self._data[i]
            self.SiftDown(minIndex, n)

    def BuildHeap(self, array, n):
        for i in range(n//2, 0, -1):
            self.SiftDown(i, n)

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
