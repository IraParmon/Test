#Дан список из целых чисел .
# Выведите все локальные максимумы (элементы с
#края не учитываются)

my_list = [1, 4, 2, 6, 3, 10, 9]
if my_list[0] < my_list[1] > my_list[2]:
    print(my_list[1])
if my_list[1] < my_list[2] > my_list[3]:
    print(my_list[2])
if my_list[2] < my_list[3] > my_list[4]:
    print(my_list[3])
if my_list[3] < my_list[4] > my_list[5]:
    print(my_list[4])
if my_list[4] < my_list[5] > my_list[6]:
    print(my_list[5])
