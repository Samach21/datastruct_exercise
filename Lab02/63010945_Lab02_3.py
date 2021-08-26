print('*** Odd Even ***')
def sort_data(data = [], sort = ''):
    ls = []
    if sort == 'Even':
        for i in range(len(data)):
            if i % 2 != 0: ls.append(data[i])
    else:
        for i in range(len(data)):
            if i % 2 == 0: ls.append(data[i])
    return ls
         
def solution(input = ['', '', '']):
    t, d, s = input
    if t == 'S' : d = list(d)
    else : d = d.split(' ')
    d = sort_data(d, s)
    if t == 'S' : return ''.join(d)
    else : return d

input = input('Enter Input : ').split(',')
print(solution(input))
