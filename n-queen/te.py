class LinkedList:
    class Node :
        def __init__(self,data,next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
                
        def __str__(self) :
            return str(self.data)

    def __init__(self, head = None):
        if head == None:
                self.head = self.tail = None
                self.size = 0
        else:
            self.head = head
            t = self.head        
            self.size = 1
            while t.next != None :
                t = t.next
                self.size += 1
            self.tail = t
            
    def __str__(self) :
        if self.isEmpty():
            return 'Empty Linked'
        s = 'Linked data : '
        p = self.head
        while p != None :
            s += str(p.data)+' '
            p = p.next
        return s

    def __len__(self) :
        return self.size
    
    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p   
            self.tail =p  
        self.size += 1

    def removeHead(self) :
        if self.head == None : return
        if self.head.next == None :
            p = self.head
            self.head = None
        else :
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data
    
    def isEmpty(self) :
        return self.size == 0
    
    def nodeAt(self,i) :
        p = self.head
        for j in range(i) :
            p = p.next
        return p

    def deleteAfter(self,i) :
        if self.size > 0 :
          q = self.nodeAt(i)
          p = q.next
          q.next = q.next.next
          self.size -= 1
          return (i + 1, p)

    def index(self,data) :
        p = self.head
        for i in range(len(self)) :
            if p.data == data :
                return i
            p = p.next
        return -1

    def isIn(self,data) :
        return self.index(data) >= 0

    def delete(self,i) :
        if i == 0 and self.size > 0 :
            p = self.head
            self.head = self.head.next
            self.size -= 1
            return (i, p)
        else :
            out = self.deleteAfter(i-1)
            return out
    
    def remove(self,data) :
        if self.isIn(data) :
            i, p = self.delete(self.index(data))
            return p

    def contentEquivalence(self, ls) -> bool:
        if len(self) != len(ls):
            return False
        for i in range(len(self)):
            for j in range(len(ls)):
                if self.nodeAt(i).data == ls.nodeAt(j).data:
                    ls.remove(ls.nodeAt(j).data)
                    break
        if len(ls) == 0:
            return True
        else:
            return False

