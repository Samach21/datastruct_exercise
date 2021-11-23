def clearList(l: list):
    di = dict()
    ls = list(l)
    for i in range(len(l)):
        if l[i] < 0:
            di[i] = l[i]
            ls.remove(l[i])
    return ls, di

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

ls = list(map(int, input('Enter Input : ').split()))

ls, dict_ls = clearList(ls)

ls = bubble(ls)

for k, v in dict_ls.items():
    ls.insert(k, v)

for i in ls:
    print(i, end=' ')