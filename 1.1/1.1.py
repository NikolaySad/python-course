# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

m = int(input("Введите трехзначное число: "))
summa = 0
while m / 10 > 0:
    summa = summa + m % 10
    m = m // 10
print(summa)