a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = (a + b) / 2
if ((c % 1) == 0):
    print('NO')
elif ((c % 1) != 0):
    print('YES') 
