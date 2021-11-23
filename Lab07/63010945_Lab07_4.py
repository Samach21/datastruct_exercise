class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)
        return self.root

    def _insert(self, root, data):
        if root is None:
            root = Node(data)
        else:
            if root.data > data:
                if root.left is None:
                    root.left = Node(data)
                else:
                    self._insert(root.left, data)
            else:
                if root.right is None:
                    root.right = Node(data)
                else:
                    self._insert(root.right, data)
        return root

    def delete(self,r, data):
        if r is None:
            print('Error! Not Found DATA')
            return r
        if data < r.data:
            r.left = self.delete(r.left, data)
        elif(data > r.data):
            r.right = self.delete(r.right, data)
        else:
            if r.left is None:
                temp = r.right
                r = None
                return temp
            elif r.right is None:
                temp = r.left
                r = None
                return temp
            temp = self.minValueNode(r.right)
            r.data = temp.data
            r.right = self.delete(r.right, temp.data)
        return r
    
    def minValueNode(self, node):
        current = node
        while(current.left is not None):
            current = current.left
        return current
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",") #i 3,i 5,i 2,d 3
for i in data:
    i = i.split()
    i[-1] = int(i[-1])
    if i[0] == 'i':
        print(f'insert {i[-1]}')
        tree.insert(i[-1])
    else:
        print(f'delete {i[-1]}')
        tree.root = tree.delete(tree.root, i[-1])
    printTree90(tree.root)