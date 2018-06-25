# python3
import time, heapq

class Heap:
    def __init__(self):
        self._data = []

    def Parent(self, i):
        return (i-1)//2

    def LeftChild(self, i):
        return 2*i+1

    def RightChild(self, i):
        return 2*i+2

    def SiftUp(self, i):
        while i > 0 and self._data[self.Parent(i)][1] > self._data[i][1]:
            self._data[self.Parent(i)], self._data[i] = self._data[i], self._data[self.Parent(i)]
            i = self.Parent(i)

    def SiftDown(self, i):
        n = len(self._data)-1
        minIndex = i
        left = self.LeftChild(i)
        right = self.RightChild(i)
        if left <= n:
            if self._data[left][1] < self._data[minIndex][1]:
                minIndex = left
            elif self._data[left][1] == self._data[minIndex][1] and self._data[left][0] < self._data[minIndex][0]:
                minIndex = left
        if right <= n:
            if self._data[right][1] < self._data[minIndex][1]:
                minIndex = right
            elif self._data[right][1] == self._data[minIndex][1] and self._data[right][0] < self._data[minIndex][0]:
                minIndex = right
        if i != minIndex:
            self._data[i], self._data[minIndex] = self._data[minIndex], self._data[i]
            self.SiftDown(minIndex)

    def Insert(self, p):
        self._data.append(p)
        self.SiftUp(len(self._data)-1)

    def ExtractMax(self):
        size = len(self._data)-1
        result = self._data[0]
        self._data[0] = self._data[size]
        size -= 1
        self.SiftDown(0)
        self._data.pop()
        return result

    def Output(self):
        print(self._data)

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def assign_jobs(self):
        self.result = []
        self.priority_queue = []
        for i in range(self.num_workers):
            self.priority_queue += [[0,i]]
        for job in self.jobs:
            thread = heapq.heappop(self.priority_queue)
            self.result.append([thread[1], thread[0]])
            thread[0] = thread[0] + job
            heapq.heappush(self.priority_queue, thread)


    def write_response(self):
        for worker_id, start_time in self.result:
            print(worker_id, start_time)


    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
