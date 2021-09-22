class Stack:
    def __init__(self, list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def __str__(self):
        s = []
        for ele in self.items:
            s.append(str(ele))
        s.reverse()
        return ''.join(s)
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
    
def dec2bin(decnum):

    s = Stack()

    while decnum > 0:
        decnum = decnum / 2
        binum = int(int(str(decnum).split('.')[-1]) / 5)
        s.push(binum)
        decnum = int(decnum)
    return s

print(" ***Decimal to Binary use Stack***")

token = input("Enter decimal number : ")

print("Binary number : ",end='')

print(dec2bin(int(token)))