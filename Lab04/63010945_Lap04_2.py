from collections import deque
class Queue:
    def __init__(self, q = None):
      if q == None:
        self.items = deque()
      else:
        self.items = deque(q,len(q))
    def __str__(self):
        s = '['
        for i, ele in enumerate(self.items):
          if i != self.size()-1:
            s += repr(str(ele))+', '
          else:
            s += repr(str(ele))
        return s + ']'
    def enQueue(self, i):
      self.items.append(i)

    def deQueue(self):
      return self.items.popleft()

    def isEmpty(self):
      return len(self.items) == 0

    def size(self):
      return len(self.items)

people = list(input('Enter people : '))

q = Queue(people)
q1 = Queue()
q2 = Queue()

min = 1
minadd1 = 0
minadd2 = 0
while q.size() != 0:
    if q1.size() < 5 or min - minadd1 == 3 and not q1.isEmpty():
        q1.enQueue(q.deQueue())
        if minadd1 == 0:
            minadd1 = min 
    elif q2.size() < 5 or min - minadd2 == 2 and not q2.isEmpty():
        q2.enQueue(q.deQueue())
        if minadd2 == 0:
            minadd2 = min
    if min - minadd1 == 3 and not q1.isEmpty():
        q1.deQueue()
        minadd1 = min
    if min - minadd2 == 2 and not q2.isEmpty():
        q2.deQueue()
        minadd2 = min
    print('{} {} {} {}'.format(min, q, q1, q2))
    min += 1
