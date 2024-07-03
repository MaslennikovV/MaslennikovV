print (f'Введите число: ')
n = int(input())
print (f"Введите {n} чисел: ")
spisok = []
for i in range(n):
    a = int(input())
    spisok.append(a)
spisok.reverse()
print(spisok)