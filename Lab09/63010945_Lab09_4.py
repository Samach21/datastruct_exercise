def bubble(l: list):
    for last in range(len(l) - 1, -1, -1):
        swaped = False
        for i in range(last):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                swaped = True
        if not swaped:
            break
    return l

def mySort(l: list):
    cop = list(l)
    for i in range(len(l)):
        for j in l[i]:
            try:
                int(j)
            except:
                l[i] = ord(j)
    l = bubble(l)
    for i in range(len(l)):
        l[i] = chr(l[i])
        for j in cop:
            if l[i] in j:
                l[i] = j
    return l

ls = input('Enter Input : ').split()

ls = mySort(ls)

for i in ls:
    print(i, end=' ')