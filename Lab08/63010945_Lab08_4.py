def sumPower(ls, n, sum = 0):
    if n >= len(ls):
        return sum
    else:
        sum += ls[n]
        return sum + sumPower(ls, (2 * n) + 1) + sumPower(ls, (2 * n) + 2)

power, compare = input('Enter Input : ').split('/')
power = list(map(int, power.split()))
compare = list(map(lambda b: list(map(int, b)),list(map(lambda a: a.split(),compare.split(',')))))

print(sum(power))
for i in compare:
    a = sumPower(power, i[0])
    b = sumPower(power, i[1])
    if a == b:
        print(f'{i[0]}={i[1]}')
    elif a > b:
        print(f'{i[0]}>{i[1]}')
    else:
        print(f'{i[0]}<{i[1]}')