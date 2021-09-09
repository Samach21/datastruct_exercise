class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
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

data = list(input("Enter expresion : "))
syb1 = '[{('
syb2 = ']})'
stack = Stack()
isError = False
for c in data:
    if c in syb1:
        stack.push(c)
    elif c in syb2:
        if stack.isEmpty():
            print(''.join(data) + ' close paren excess')
            isError = True
            break
        else:
            for i in range(len(syb2)):
                if c == syb2[i]:
                    c = syb1[i]
            if stack.pop() != c:
                print(''.join(data) + ' Unmatch open-close')
                isError = True
                break
if not isError:
    if not stack.isEmpty():
        print(''.join(data) + ' open paren excess' + '   {} : {}'.format(str((stack.size())), stack))
    else:
        print(''.join(data), 'MATCH')


