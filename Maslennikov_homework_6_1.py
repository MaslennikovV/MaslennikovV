n = int(input('Введите количество чисел: '))
null = 0
for i in range(n):
    chislo = int(input(f"Введите {i+1} число: "))
    if chislo == 0:
        null += 1

print(f"Количество чисел равных Нулю: {null}")