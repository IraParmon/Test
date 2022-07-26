#Дан список с числами, все элементы различны. Поменяйте местами максимальный и
# минимальный элемент и выведите новый список.

a=[int(i) for i in input().split()]
max=a.index(max(a))
min=a.index(min(a))
a[max],a[min]=a[min],a[max]
print(a)

