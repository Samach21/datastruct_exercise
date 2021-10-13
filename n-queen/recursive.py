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
