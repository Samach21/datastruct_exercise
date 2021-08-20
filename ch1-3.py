print(' *** Summation of each digit ***')
items = input('Enter a positive number : ')
items = list(map(int, list(items)))
print('Summation of each digit =  {}'.format(sum(items)))