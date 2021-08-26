def weirdSubtract(n,k):
    n = list(map(int,list(str(n))))
    for _ in range(k):
        if len(n) == 0:
            return 0
        if n[-1] == 0:
            n.pop()
        else :
            n[-1] -= 1
    return int(''.join(list(map(str, n))))

n,s = input("Enter num and sub : ").split()

print(weirdSubtract(int(n),int(s)))