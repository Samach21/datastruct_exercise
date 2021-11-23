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

def closestValue(root: Node, value: int):
    if value == root.data:
        return root.data
    elif value < root.data:
        if root.left is not None:
            if root.data - value > abs(root.left.data - value):
                if root.left.right is not None:
                    if abs(root.left.right.data - value) < abs(root.left.data - value) and abs(root.left.right.data - value) < abs(root.data - value):
                        return closestValue(root.left.right, value)
                return closestValue(root.left, value)
            else:
                if root.left.right is not None:
                    if abs(root.left.right.data - value) < abs(root.left.data - value) and abs(root.left.right.data - value) < abs(root.data - value):
                        return closestValue(root.left.right, value)
                return root.data
        else:
            return root.data
    else:
        if root.right is not None:
            if abs(root.data - value) > abs(root.right.data - value):
                if root.right.left is not None:
                    if abs(root.right.left.data - value) < abs(root.right.data - value) and abs(root.right.left.data - value) < abs(root.data - value):
                        return closestValue(root.right.left, value)
                return closestValue(root.right, value)
            else:
                if root.right.left is not None:
                    if abs(root.right.left.data - value) < abs(root.right.data - value) and abs(root.right.left.data - value) < abs(root.data - value):
                        return closestValue(root.right.left, value)
                return root.data
        else:
            return root.data

data, target = input('Enter Input : ').split('/')
data = list(map(int, data.split()))
target = int(target)

T = BST()
for i in data:
    root = T.insert(i)
    printTree(root)
    print('--------------------------------------------------')
print(f'Closest value of {target} : {closestValue(root, target)}')