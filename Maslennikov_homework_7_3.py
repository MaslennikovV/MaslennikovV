print ('Какой вес в кг может перевезти одна лодка?: ')
m = int(input())
print ('Сколько рыбаков стоят на берегу?: ')
n = int(input())
print (f'Введите вес каждого рыбака: ')
spisok = []
ryb = 0
for i in range(n):
    a = int(input())
    spisok.append(a)
    if a > m:
        print ('Замените толстяка')
        spisok.remove(a)
        a = int(input())
        spisok.append(a)
    else:
        ryb = ryb + a
lodok = ryb/m
if lodok < 1:
    lodok = 1
else: 
    lodok = round(lodok) + 1
print(f'Минимально необходимо следующее количество лодок: {lodok}')