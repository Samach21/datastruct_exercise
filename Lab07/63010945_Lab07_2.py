class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self) -> str:
        return str(self.data)

class BST:
    def __init__(self) :
        self.root = None

    def insert(self, i):
        self.root = self.binary_insert(self.root, i)
        return self.root

    def binary_insert(self, root, data):
        if root is None:
            root = Node(data)
        else:
            if root.data > data:
                if root.left is None:
                    root.left = Node(data)
                else:
                    self.binary_insert(root.left, data)
            else:
                if root.right is None:
                    root.right = Node(data)
                else:
                    self.binary_insert(root.right, data)
        return root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def min(self, root):
        if root.left is None:
            return root
        return self.min(root.left)
    
    def max(self, root):
        if root.right is None:
            return root
        return self.max(root.right)

T = BST()

inp = [int(i) for i in input('Enter Input : ').split()]

for i in inp:
    root = T.insert(i)
T.printTree(root)

print('-' * 50)

print(f'Min : {T.min(root)}')
print(f'Max : {T.max(root)}')
