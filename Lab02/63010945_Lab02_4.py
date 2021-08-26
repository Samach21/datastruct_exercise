data = list(map(int, input('Enter Your List : ').split()))
def fn(data):
    ls = []
    for i in range(len(data)):
        triLs = []
        data2 = list(data)
        triLs.append(data2[i])
        del data2[i]
        for j in range(len(data2)):
            data3 = list(data2)
            triLs2 = list(triLs)
            triLs2.append(data3[j])
            del data3[j]
            for k in data3:
                triLs3 = list(triLs2)
                triLs3.append(k)
                triLs3.sort()
                if sum(triLs3) == 0 and triLs3 not in ls:
                    ls.append(triLs3)
    return ls

if len(data) <= 2: print('Array Input Length Must More Than 2')  
else:
    print(fn(data))