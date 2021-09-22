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

ActivityMapper = ['Eat', 'Game', 'Learn', 'Movie']
LocationMapper = ['Res.', 'ClassR.', 'SuperM.', 'Home']

def dataToAL(s: str) -> str:
    return ActivityMapper[int(s[0])] + ':' + LocationMapper[int(s[-1])]

def Mapper(s: str) -> str:
    s = s.split(', ')
    for i in range(len(s)):
        s[i] = dataToAL(s[i])
    return ', '.join(s)

def predictLove(a: Queue, b:Queue) -> str:
    score = 0
    while a.size() > 0:
        data1 = a.deQueue()
        data2 = b.deQueue()
        if data1[0] == data2[0] and  data1[-1] != data2[-1]:
            score += 1
        elif data1[0] != data2[0] and  data1[-1] == data2[-1]:
            score += 2
        elif data1[0] == data2[0] and  data1[-1] == data2[-1]:
            score += 4
        else:
            score -= 5
    if score >= 7:
        return '''Yes! You're my love! : Score is {}.'''.format(score)
    elif score > 0:
        return '''Umm.. It's complicated relationship! : Score is {}.'''.format(score)
    else:
        return '''No! We're just friends. : Score is {}.'''.format(score)

inp = input('Enter Input : ').split(',')

myQueue = Queue()
yourQueue = Queue()

for i in inp:
    my, your = i.split()
    myQueue.enQueue(my)
    yourQueue.enQueue(your)

print('My   Queue = ' + str(myQueue))
print('Your Queue = ' + str(yourQueue))
print('My   Activity:Location = ' + Mapper(str(myQueue)))
print('Your Activity:Location = ' + Mapper(str(yourQueue)))
print(predictLove(myQueue, yourQueue))