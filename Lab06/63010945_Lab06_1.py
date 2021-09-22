def print1ToN(n):
    if n <= 0 :
        print(1, end= ' ')
        return
    if n > 1 :
        print1ToN(n - 1)
    print(n, end=' ')
    
def printNto1(n):
    if n <= 0 :
        print(1, end= ' ')
        return
    print(n, end=' ')
    if n > 1 :
        printNto1(n - 1)

n = int(input("Enter Input : "))

print1ToN(n)
printNto1(n)