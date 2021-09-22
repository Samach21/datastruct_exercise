def pantip(k:int, n:int, arr:list, path:list):
    if len(arr)!= 0:
        path.append(arr.pop(0))
    if sum(path) == 20:
        if len(path) != 1:
            arr.append(path.pop())
        else:
            path.pop()
    else if
    

inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [])
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))