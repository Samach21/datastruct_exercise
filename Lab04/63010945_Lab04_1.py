from collections import deque
class Queue:
    def __init__(self, q = None):
      if q == None:
        self.items = deque()
      else:
        self.items = deque(q,len(q))
    def __str__(self):
        if (self.isEmpty()):
          return "Empty"
        s = ''
        for i, ele in enumerate(self.items):
          if i != self.size()-1:
            s += str(ele)+' '
          else:
            s += str(ele)
        return s
    def enQueue(self, i):
      self.items.append(i)

    def deQueue(self):
      return self.items.popleft()

    def isEmpty(self):
      return len(self.items) == 0

    def size(self):
      return len(self.items)

inp = input('Enter Input : ').split(',')

q = Queue()

for i in inp:
    if len(i) > 1:
        q.enQueue(int(i.split()[-1]))
        print(q.size())
    else:
        try:
            print('{} 0'.format(q.deQueue()))
        except:
            print(-1)
print(q)