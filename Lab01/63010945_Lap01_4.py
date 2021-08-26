print(" ***Function Odd List***")
def odd_list(ls):
    result = []
    for ele in ls:
        if ele % 2 != 0:
            result.append(ele)
    return result
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)