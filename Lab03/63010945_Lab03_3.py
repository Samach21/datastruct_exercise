class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        s = 'stack of '+ str(self.size())+' items : '
        for ele in self.items:
            s += str(ele)+' '
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

inp = input('Enter Input : ').split()

S = Stack()

combo = 0
for i in inp:
    if S.size() < 2:
        S.push(i)
    else:
        c1 = S.pop()
        c2 = S.pop()
        if i != c1 or i != c2:
            S.push(c2)
            S.push(c1)
            S.push(i)
        else:
            combo += 1

print(S.size())

if S.size() > 0:
    for _ in range(S.size()):
        print(S.pop(), end="")
    print()
else:
    print('Empty')

if combo > 1:
    print('Combo : {} ! ! !'.format(combo))