# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с 
# номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать 
# программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

ticket = int(input('Введите шестизначное число: '))
summa1 = 0
v = ticket % 1000
while v / 10 > 0:
    summa1 = summa1 + v % 10
    v = v // 10

summa2 = 0
v = ticket // 1000
while v / 10 > 0:
    summa2 = summa2 + v % 10
    v = v // 10

if summa1 == summa2:
    print('Yes')
else:
    print('No')