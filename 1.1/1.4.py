# Задача 8: Требуется определить, можно ли от шоколадки размером 
# n × m долек отломить k долек, если разрешается сделать один 
# разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите n размер шоколадки: "))
m = int(input("Введите m размер шоколадки: "))

k = int(input("Введите кол-во долек, которое хотите отломить: "))

if k < m * n and k % 2 == 0:
    print('Yes')
else:
    print('No')