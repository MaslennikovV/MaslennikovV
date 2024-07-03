a = input ()
a = a.split(' ')
n = 0
while n < len(a):
    if a[n] == '':
        del a[n]
    else:
        n += 1
a = ' '.join(a)
print(a)