class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
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

def printTree(node, level = 0):
        if node != None:
            printTree(node.right, level + 1)
            print('     ' * level, node)
            printTree(node.left, level + 1)

def minTree(root):
    if root.left is None:
        return root.data
    else:
        return minTree(root.left)

def search(root, key):
    if root is None:
        return False
    else:
        if root.data == key:
            return True
        elif root.data < key:
            return search(root.right,key)
        else: 
            return search(root.left, key)



data, target = input('Enter Input : ').split('/')
data = list(map(int, data.split()))
target = int(target)

T = BST()
for i in data:
    root = T.insert(i)
printTree(root)
print('--------------------------------------------------')

i = minTree(root)
rank = 0
while i <= target:
    if search(root, i):
        rank += 1
    i += 1

print(f'Rank of {target} : {rank}')