#Дан список из целых чисел . Записать все числа в кортеж и вывести
#уникальные значения

l=[int(x) for x in input().split()]
l_tuple = tuple(l)
for i in l_tuple:
    if l_tuple.count(i) == 1:
        print(i)