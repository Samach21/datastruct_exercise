def insertion(l: list):
    ols = [l.pop(0)]
    while len(l) != 0:
        a = l.pop(0)
        index = 0
        for i in range(len(ols)):
            if a > ols[i]:
                index += 1
        ols.insert(index, a)
        print(f'insert {a} at index {index} : {ols} {ls if len(ls) != 0 else ""}')
    print('sorted')
    return ols

ls = list(map(int, input('Enter Input : ').split()))

print(insertion(ls))