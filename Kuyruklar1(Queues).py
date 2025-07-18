from collections import deque
import heapq

# FIFO Kuyruk (Queue)
class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.popleft()
    
    def is_empty(self):
        return not self.items

# Dairesel Kuyruk (Circular Queue)
class CircularQueue:
    def __init__(self, size):
        self.queue = [None]*size
        self.max_size = size
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.max_size == self.front:
            print("Queue is Full")
            return
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = item
        print(f"Eklendi: {item} | Kuyruk durumu: {self.queue}")

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
            return
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        print(f"Çıkarıldı: {item} | Kuyruk durumu: {self.queue}")
        return item

# Öncelikli Kuyruk (Priority Queue)
class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item, priority):
        heapq.heappush(self.queue, (priority, item))
        print(f"Eklendi: {item} (öncelik: {priority}) | Kuyruk durumu: {[i[1] for i in self.queue]}")
    
    def dequeue(self):
        item = heapq.heappop(self.queue)[1]
        print(f"Çıkarıldı: {item} | Kuyruk durumu: {[i[1] for i in self.queue]}")
        return item

# Çift Taraflı Kuyruk (Deque)
dq = deque()
print("Başlangıç deque:", dq)

dq.append('sağdan eklendi')
print("append (sağdan):", dq)

dq.appendleft('soldan eklendi')
print("appendleft (soldan):", dq)

pop_son = dq.pop()
print("pop (sağdan çıkarıldı):", pop_son)
print("Deque durumu:", dq)

pop_ilk = dq.popleft()
print("popleft (soldan çıkarıldı):", pop_ilk)
print("Deque durumu:", dq)
