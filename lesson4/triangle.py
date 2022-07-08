def get_square2(a, b, c):
    if a==0 or b==0 or c==0:
        raise Exception("Сторона не равна 0")
    else:
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def get_perim2(a, b, c):
    return (a + b + c)

