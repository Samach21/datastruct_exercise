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

