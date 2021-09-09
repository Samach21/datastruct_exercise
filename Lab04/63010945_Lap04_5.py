from collections import deque
class Queue:
    def __init__(self, q = None):
        if q == None:
            self.items = deque()
        else:
            self.items = deque(q)
    def __str__(self):
        s = ''
        for i, ele in enumerate(self.items):
          if i != self.size()-1:
            s += str(ele)+', '
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

    def to_list(self):
        return list(self.items)

class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        if self.isEmpty():
            return 'ytpmE'
        s = ''
        for ele in self.items:
            s += str(ele)
        return s
    def push(self, i):
        self.items.append(i)

    def pop(self): 
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

normal, mirror = input('Enter Input (Normal, Mirror) : ').split()

normalStack = Stack()
mirrorStack = Stack(list(mirror))
saveMirrorStack = Stack()
mirrorQueue = Queue()
normalExplo = 0
mirrorExplo = 0
fail = 0

while mirrorStack.size() > 2:
    c1 = mirrorStack.pop()
    c2 = mirrorStack.pop()
    c3 = mirrorStack.pop()
    if c1 == c2 and c1 == c3:
        mirrorQueue.enQueue(c1)
        mirrorExplo += 1
        while saveMirrorStack.size() > 0:
            mirrorStack.push(saveMirrorStack.pop())
    else:
        saveMirrorStack.push(c1)
        mirrorStack.push(c3)
        mirrorStack.push(c2)

while saveMirrorStack.size() > 0:
    mirrorStack.push(saveMirrorStack.pop())

for i in normal:
    if normalStack.size() < 2:
        normalStack.push(i)
    else:
        c1 = normalStack.pop()
        c2 = normalStack.pop()
        if i != c1 or i != c2:
            normalStack.push(c2)
            normalStack.push(c1)
            normalStack.push(i)
        else:
            if not mirrorQueue.isEmpty():
                c3 = mirrorQueue.deQueue()
                if c3 == i:
                    fail += 1
                    normalStack.push(c2)
                else:
                    normalStack.push(c2)
                    normalStack.push(c1)
                    normalStack.push(c3)
                    normalStack.push(i)
            else:
                normalExplo += 1

print('NORMAL :')
print(normalStack.size())
normalStack = list(str(normalStack))
normalStack.reverse()
print(''.join(normalStack))
print('{} Explosive(s) ! ! ! (NORMAL)'.format(normalExplo))
if fail > 0:
    print('Failed Interrupted {} Bomb(s)'.format(fail))
print('------------MIRROR------------')
print(': RORRIM')
print(mirrorStack.size())
print(mirrorStack)
print('(RORRIM) ! ! ! (s)evisolpxE {}'.format(mirrorExplo))