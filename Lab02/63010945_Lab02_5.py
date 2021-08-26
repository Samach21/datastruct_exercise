def bon(w = ''):
    target = ''
    for i in list(w):
        ls = list(w)
        ls.remove(i)
        if i in ls:
            target = i
            break
    return (ord(target) - 96) * 4
        
        
secretCode = input("Enter secret code : ")
print(bon(secretCode))