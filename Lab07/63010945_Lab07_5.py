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
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def checkpos(self, data):
        if self.root.data == data:
            print("Root")
            return
        def helper(r, data):
            if r is None:
                print("Not exist")
                return
            if data < r.data:
                r.left = helper(r.left, data)
            elif data > r.data:
                r.right = helper(r.right, data)
            else:
                if r.right is None and r.left is None:
                    print("Leaf")
                    return
                else:
                    print("Inner")
                    return
        return helper(self.root, data)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
T.checkpos(inp[0])