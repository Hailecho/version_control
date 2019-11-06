x= int(input('Give your number of sides: '))
r = int(input('Give your second number: '))
m = len(str(x*r))

for i in range(r+1):
    t = len(str(x*i))
    k = len(str(r))-len(str(i))
    # print(x, ' times ',' '*k, i,' = ',' '*(m-t), x*i, sep='')

# Another way of doing it is using sequence of print with end option:

for i in range(r + 1):
    t = len(str(x*i))
    k = len(str(r))-len(str(i))
    print(x, 'times', end='')
    print(' '*k, i,'=', end='')
    print(' '*(m-t), x*i)
    # print(x, ' times ',' '*k, i,' = ',' '*(m-t), x*i)

# add examples here 

