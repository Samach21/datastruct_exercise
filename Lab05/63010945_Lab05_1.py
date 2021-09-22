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
        if self.isEmpty():
            return "Empty"
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
          self.insertAfter(len(self)-1,data)
    
    def insertAfter(self,i,data) :
        q = self.nodeAt(i)
        p = self.Node(data)
        p.next = q.next
        q.next = p
        self.Size += 1
    
    def deleteAfter(self,i) :
        if self.Size > 0 :
          q = self.nodeAt(i)
          q.next = q.next.next
          self.Size -= 1
    
    def delete(self,i) :
        if i == 0 and self.Size > 0 :
          self.head = self.head.next
          self.Size -= 1
        else :
          self.deleteAfter(i-1)
        
    def removeData(self,data) :
        if self.isIn(data) :
            self.deleteAfter(self.indexOf(data)-1)
          
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
        return str(len(self))

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
    
    def search(self, data):
        if self.index(data) >= 0:
            return 'Found {} in {}'.format(data, str(self))
        else:
            return 'Not Found {} in {}'.format(data, str(self))

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0}".format(L.search(i[3:])))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)