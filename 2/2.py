#На входе список из чисел, каждое число повторяется два раза,
#и только одно число повторяется 1 раз. Найти число, которое повторяется 1 раз.

#пример:
#1 6 2 5 2 9 6 1 5
#вывести 9

a = input().split()
l = []
for i in range(len(a)):
    l.append(a[i])

for i in l:
    if l.count(i) == 1:         #если элемент повторяется 1 раз
        print(i)

