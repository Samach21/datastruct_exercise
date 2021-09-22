from collections import deque
class Queue:
    def __init__(self, q = None):
        if q == None:
            self.items = deque()
        else:
            self.items = deque(q)
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

    def to_list(self):
        return list(self.items)

q, inp = input('Enter Input : ').split('/')
q = q.split()
q = Queue(q)
inp = inp.split(',')

for i in inp:
    if len(i) > 1:
        q.enQueue(i.split()[-1])
    else:
        q.deQueue()

ls = []
while q.size() != 0:
    ls.append(q.deQueue())

isDup = False
for i in ls:
    copy_ls = list(ls)
    copy_ls.remove(i)
    if i in copy_ls:
        isDup = True
        break
print('Duplicate') if isDup else print('NO Duplicate')