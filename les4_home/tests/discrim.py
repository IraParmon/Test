# Написать функцию принимающую три агрумента - коэффициенты A, B и C
# квадратного уравнения function1
# функция должна выводить действительные корни квадратного уравнения

def get_koren(A, B, C):
    D = (B ** 2 - 4 * A * C)
    x1 = (-B - D ** 0.5) / 2 * A
    x2 = (-B + D ** 0.5) / 2 * A

    if D == 0:
        return int(-B / 2 * A)
    elif D > 0:
        return f"{int(x1)}, {int(x2)}"
    elif D < 0:
        return "Нет корней"
