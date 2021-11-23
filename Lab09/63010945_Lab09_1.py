def isSorted(l: list) -> bool:
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True

ls = list(map(int, input('Enter Input : ').split()))

if isSorted(ls):
    print('Yes')
else:
    print('No')
