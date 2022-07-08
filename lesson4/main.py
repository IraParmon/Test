from lesson4.circle import get_square
from lesson4.rectangle import get_perim3, get_square3
from lesson4.triangle import get_square2, get_perim2

r = int(input("Введите радиус: "))
print(get_square(r))

a = int(input("Введите a треугольника: "))
b = int(input("Введите b треугольника: "))
c = int(input("Введите c треугольника: "))

print(get_square2(a, b, c))
print(get_perim2(a, b, c))

d = int(input("Введите ширину прямоугольника: "))
e = int(input("Введите высоту прямоугольника: "))
print(get_square3(d, e))
print(get_perim3(d, e))
