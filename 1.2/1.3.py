# Задача 14: Требуется вывести все целые степени 
# двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

n = int(input('Введите число: '))
p = 2
for i in range(n):
    if 0 <= n:
        p = p ** i
        if p < n:
            print(p, end=' ')
            p = 2        
        else:
            break