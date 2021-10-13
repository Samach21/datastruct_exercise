from itertools import permutations
def nqueen_iterative(N):

    def print_table():
        nonlocal N
        for row in range(N):
            print([0 if i == 1 else 1 for i in table[row]])

    def put_queen(x,y):
        nonlocal N
        if table[y][x] == 0:
            for m in range(N):
                table[y][m] = 1
                table[m][x] = 1
                table[y][x] = 2
                if y+m <= N-1 and x+m <= N-1:
                    table[y+m][x+m] = 1
                if y-m >= 0 and x+m <= N-1:
                    table[y-m][x+m] = 1
                if y+m <= N-1 and x-m >= 0:
                    table[y+m][x-m] = 1
                if y-m >= 0 and x-m >= 0:
                    table[y-m][x-m] = 1
            return True
        else:
            return False

    table = [[0]*N for _ in range(N)]
    perms = permutations([i for i in range(N)])
    num_comb = 0

    for perm in perms:
        is_solution = True
        for i in range(N):
            is_solution = is_solution and put_queen(perm[i], i)
        if is_solution:
            print_table()
            num_comb += 1
        table = [[0] * N for _ in range(N)]
        
    print(f'number of solutions : {num_comb}')

def nqueen_recursive(N):
    numSol = 0
    b = N*[-1]
    colFree = N*[1]
    upFree = (2*N - 1)*[1]
    downFree = (2*N - 1)*[1]
    def printBoard(b):
        for row in range(N):
            print([0 if i != b[row] else 1 for i in range(N)])
        print()
    def putQueen(r, b, colFree, upFree, downFree):
        nonlocal N
        nonlocal numSol
        for c in range(N):
            if colFree[c] and upFree[r+c] and downFree[r-c+N-1]:
                b[r] = c
                colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 0
                if r == N-1:
                    printBoard(b)
                    numSol += 1
                else:
                    putQueen(r+1, b, colFree, upFree, downFree)
                colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 1
                
    putQueen(0, b, colFree, upFree, downFree)
    print(f'number of solutions : {numSol}')

