print('*** Rabbit & Turtle ***')
d, Vr, Vt, Vf =  list(map(int, input("Enter Input : ").split()))
print('{:.2f}'.format(Vf * d/(Vt-Vr)))