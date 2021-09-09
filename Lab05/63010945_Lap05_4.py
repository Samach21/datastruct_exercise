class LinkedList :
    class Node :
        def __init__(self, data, next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
        
    def __init__(self):                
            self.head = None
            self.Size = 0
            
    def __str__(self):
        s = ''
        p = self.head
        while p != None :
            s += str(p.data) + ' '
            p = p.next
        return s
          
    def __len__(self) :
        return self.Size         
            
    def isEmpty(self) :
        return self.Size == 0
        
    def index(self,data) :
        p = self.head
        for i in range(len(self)) :
            if p.data == data :
                return i
            p = p.next
        return -1
            
    def isIn(self,data) :
        return self.index(data) >= 0
    
    def nodeAt(self,i) :
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p
    
    def append(self,data):
        if self.head is None :
          p = self.Node(data)
          self.head = p
          self.Size += 1
        else :
          self.insert(len(self),data)
    
    def insert(self,i,data) :
        while i < 0 :
            raise Exception()
        if i == 0:
            q = self.nodeAt(i)
            p = self.Node(data)
            self.head = p
            p.next = q
            self.Size += 1
            return
        elif i == len(self):
            q = self.nodeAt(i - 1)
            p = self.Node(data)
            q.next = p
            self.Size += 1
            return
        else:
            q = self.nodeAt(i - 1)
            p = self.Node(data)
            p.next = q.next
            q.next = p
            self.Size += 1
            return
    
    def deleteAfter(self,i) :
        if self.Size > 0 :
          q = self.nodeAt(i)
          p = q.next
          q.next = q.next.next
          self.Size -= 1
          return (i + 1, p)
    
    def delete(self,i) :
        if i == 0 and self.Size > 0 :
            p = self.head
            self.head = self.head.next
            self.Size -= 1
            return (i, p)
        else :
            out = self.deleteAfter(i-1)
            return out
        
    def remove(self,data) :
        if self.isIn(data) :
            i, p = self.delete(self.index(data))
            return p
    def addHead(self,data) :
        if self.isEmpty() :
          p = self.Node(data)
          self.head = p
          self.Size += 1
        else :
          p = self.Node(data,self.head)
          self.head = p
          self.Size += 1
    
    def size(self):
        return len(self)

    def pop(self, i = None):
        if i is None:
            q = self.nodeAt(len(self) - 2)
            p = q.next
            q.next = None
            self.Size -= 1
            return 'Success'
        else:
            if self.isEmpty() or i >= len(self):
                return 'Out of Range'
            else:
                q = self.nodeAt(i - 1)
                p = q.next
                try:
                    q.next = q.next.next
                except:
                    q.next = None
                self.Size -= 1
                return 'Success'

inp = input('Enter Input : ').split(',')
L = LinkedList()
L.append('|')
for i in inp:
    if len(i) == 1:
        m = i
    else:
        m, data = i.split()
    index = L.index('|')
    if m == 'I':
        L.insert(index, data)
    elif m == 'L':
        if index == 0:
            continue
        else:
            L.remove('|')
            L.insert(index - 1, '|')
    elif m == 'R':
        if index == L.size() - 1:
            continue
        else:
            L.remove('|')
            L.insert(index + 1, '|')
    elif m == 'B':
        if index == 0:
            continue
        else:
            L.delete(index - 1)
    elif m == 'D':
        if index == L.size() - 1:
            continue
        else:
            L.delete(index + 1)
print(L)