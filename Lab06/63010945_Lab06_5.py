def staircase(n):
    s = ''
    def help(a, s):
        if a < 0:
            return s
        s += '_' * a
        s += '#' * (n - a)
        s += '\n'
        return help(a - 1, s)
    def help02(a, s):
        if a == n:
            return s
        s += '_' * a
        s += '#' * (n - a)
        s += '\n'
        return help02(a + 1, s)
    if n > 0:
        i = n - 1
        return help(i, s)
    elif n < 0:
        i = 0
        n = n * -1
        return help02(i, s)
    else:
        return 'Not Draw!'

print(staircase(int(input("Enter Input : "))))