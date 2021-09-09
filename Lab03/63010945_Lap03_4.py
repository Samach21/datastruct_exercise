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
    
    def to_list(self):
        return list(self.items)

S = Stack()


inp = input('Enter Input : ').split(',')

for i in inp:
    if len(list(i)) > 1:
        S.push(int(i.split()[-1]))
    elif S.size() > 0:
        n1 = S.pop()
        save = n1
        R = Stack(S.to_list())
        total = 1
        while R.size() > 0:
            n2 = R.pop()
            if n2 > n1:
                n1 = n2
                total += 1
        print(total)
        S.push(save) 
    else:
        print(S.size())