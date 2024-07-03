a = int(input('Введите число A: '))
b = int(input('Введите число B, меньшее или равное А: '))
count = 0
for i in range(b, (a+1)):
    if i%2 == 0:
        count +=1
        print (i, end = ' ')