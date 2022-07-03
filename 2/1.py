a = input().split()
l = []
for i in range(len(a)):
    l.append(a[i])
print(l)


l = [int(x) for x in a]       #преобразование каждого элемента списка из строки в число

for i in l:
    if i % 3 == 0 and i % 5 != 0:
        print("Число подходит под условия:",i)

max_number = max(l)
print("Максимальное:", max_number)
min_number = min(l)
print("Минимальное:", min_number)