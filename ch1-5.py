num = int(input('Enter Input : '))
def listTri(n, sym):
    ls = []
    for i in range(1, n + 3):
        ls.append((n + 2 - i) * '.' + (i * sym))
    if sym == '+':
        for i in range(len(ls)):
            ls[i] = ls[i][::-1]
        ls.reverse()
    return ls
def listSquare(n, sym1, sym2):
    ls = []
    for i in range(1, n + 3):
        if i == 1 or i == n + 2:
            ls.append((n + 2) * sym1)
        else :
            ls.append(sym1 + (n * sym2) + sym1)
    return ls
for i in range(num + 2):
    print(listTri(num, '#')[i] + listSquare(num, '+', '#')[i])
for i in range(num + 2):
    print(listSquare(num, '#', '+')[i] + listTri(num, '+')[i])
