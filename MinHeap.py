class MinHeap:
    def __init__(self, hlist=None):
        self.hlist = hlist if hlist else []
        if hlist:
            self.heapify()

    def heapify(self):
        for i in reversed(range(len(self.hlist)//2)):
            self.sift_down(i)

    def sift_down(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < len(self.hlist) and self.hlist[i] > self.hlist[left]:
            smallest = left
        if right < len(self.hlist) and self.hlist[smallest] > self.hlist[right]:
            smallest = right
        if smallest != i:
            self.hlist[i], self.hlist[smallest] = self.hlist[smallest], self.hlist[i]
            self.sift_down(smallest)

    def sift_up(self, i):
        parent = (i - 1) // 2
        if parent >= 0 and self.hlist[i] < self.hlist[parent]:
            self.hlist[i], self.hlist[parent] = self.hlist[parent], self.hlist[i]
            self.sift_up(parent)

    def insert(self, item):
        self.hlist.append(item)
        self.sift_up(len(self.hlist) - 1)
