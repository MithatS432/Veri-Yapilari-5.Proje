from collections import deque
import heapq

# FIFO: Müşteri Hizmetleri Kuyruğu
def process_customer_queue():
    q = Queue()
    q.enqueue("Müşteri 1")
    q.enqueue("Müşteri 2")
    q.enqueue("Müşteri 3")
    while not q.is_empty():
        print("Hizmet verilen:", q.dequeue())

# Dairesel Kuyruk: CPU Round-Robin Scheduling
def cpu_scheduler():
    cqueue = CircularQueue(3)
    cqueue.enqueue("İşlem A")
    cqueue.enqueue("İşlem B")
    cqueue.enqueue("İşlem C")
    print("İşlem alındı:", cqueue.dequeue())
    cqueue.enqueue("İşlem D")
    print("İşlem alındı:", cqueue.dequeue())

# Öncelikli Kuyruk: Acil Durum Servisi
def emergency_room():
    pq = PriorityQueue()
    pq.enqueue("Hastalık A (önemsiz)", 3)
    pq.enqueue("Hastalık B (orta)", 2)
    pq.enqueue("Hastalık C (acil)", 1)
    print("Öncelikli hasta:", pq.dequeue())
    print("Sonraki hasta:", pq.dequeue())

# Deque: Tarayıcı geçmişi ileri-geri
def browser_history():
    history = deque()
    history.append("Sayfa 1")
    history.append("Sayfa 2")
    history.append("Sayfa 3")
    print("Geri git:", history.pop())
    history.append("Sayfa 4")
    print("İleri gitme yok (yeni sayfa eklendi):", history)

# Yardımcı sınıf (FIFO için)
class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.popleft()
    
    def is_empty(self):
        return not self.items

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

    def dequeue(self):
        if self.front == -1:
            print("Queue is Empty")
            return
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size
        return item

class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item, priority):
        heapq.heappush(self.queue, (priority, item))
    
    def dequeue(self):
        return heapq.heappop(self.queue)[1]

# Fonksiyonları çalıştırma
process_customer_queue()
cpu_scheduler()
emergency_room()
browser_history()
