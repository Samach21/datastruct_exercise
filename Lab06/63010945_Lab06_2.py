def length(txt):
    i = 0
    def helper(i, str):
        if str == '':
            return 0
        print(str[0], end= '*') if i % 2 == 0 else print(str[0], end= '~')
        str = str[1:]
        i += 1
        return 1 + helper(i, str)
    return helper(i, txt)

print("\n",length(input("Enter Input : ")),sep="")
#ตรง print(เป็นแค่ตัวอย่างสามารถแก้ไขได้)