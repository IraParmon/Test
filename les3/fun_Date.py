# аписать функцию, принимающую три агрумента - день, месяц и год Вывести "OK" если дата корректна,
# "FAILED" если дата не корректа dd.mm.yyyy

def read_input():
    in_str = input().split(".")
    dd = in_str[0]
    mm = in_str[1]
    yyyy = in_str[2]
    return int(dd), int(mm), int(yyyy)


def fun_date(dd, mm, yyyy):
    if dd <= 0 or dd >= 32 or mm <= 00 or mm >= 13 or yyyy <= 0000:
        return "FALSE"
    elif dd == 31 and mm == 4 or dd == 31 and mm == 6 or dd == 31 and mm == 9 or dd == 31 and mm == 11:
        return "FALSE"
    elif dd == 30 and mm == 2 or dd == 31 and mm == 2:
        return "FALSE"

    elif yyyy % 400 == 0 and mm == 2 and dd == 29:
        return "OK"
    elif yyyy % 100 == 0 and mm == 2 and dd == 29:
        return "FALSE"
    elif yyyy % 4 == 0 and mm == 2 and dd == 29:
        return "OK"
    elif yyyy % 400 != 0 and mm == 2 and dd == 29:
        return "FALSE"
    elif yyyy % 4 != 0 and mm == 2 and dd == 29:
        return "FALSE"

    else:
        return "OK"

def fun_correct(dd, mm, yyyy):
    if dd <= 0 or dd >= 32 or mm <= 00 or mm >= 13 or yyyy <= 0000:
        return "Incorrect day"
    elif dd == 31 and mm == 4 or dd == 31 and mm == 6 or dd == 31 and mm == 9 or dd == 31 and mm == 11:
        return "Incorrect day"
    elif dd == 30 and mm == 2 or dd == 31 and mm == 2:
        return "Incorrect day"
    else:
        return ""