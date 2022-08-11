import sqlite3
from datetime import datetime

DATE=datetime.now().date()

def create_table_inc(DATE, INCOME, SUM):
    con = sqlite3.connect('date.db')
    cur = con.cursor()

    cur.execute(
        f"""
            INSERT INTO income
            (DATE, INCOME, SUM)
            VALUES('{DATE}', '{INCOME}', '{SUM}');
        """
    )
    con.commit()
    con.close()

def create_table_exp(DATE, EXPENSE, SUM):
    con = sqlite3.connect('date.db')
    cur = con.cursor()

    cur.execute(
        f"""
            INSERT INTO expenses
            (DATE, INCOME, SUM)
            VALUES('{DATE}', '{EXPENSE}', '{SUM}');
        """
    )
    con.commit()
    con.close()


def get_all_users():
    con = sqlite3.connect('date.db')
    cur = con.cursor()

    res = cur.execute(
        f""" SELECT * FROM income; """
    )
    res = res.fetchall()
    con.close()
    return res




def get_sum():
    con = sqlite3.connect('date.db')
    cur = con.cursor()

    res = cur.execute(
        f""" SELECT SUM(SUM) FROM income; """
    )
    res = res.fetchall()
    con.close()
    return res


def get_sum1():
    con = sqlite3.connect('date.db')
    cur = con.cursor()

    res = cur.execute(
        f""" SELECT SUM(SUM) FROM income WHERE INCOME='Зарплата'; """
    )
    res = res.fetchall()
    con.close()
    return res

def get_sum2():
    con = sqlite3.connect('date.db')
    cur = con.cursor()

    res = cur.execute(
        f""" SELECT SUM(SUM) FROM income WHERE INCOME='Перевод'; """
    )
    res = res.fetchall()
    con.close()
    return res

def get_sum_August():
    con = sqlite3.connect('date.db')
    cur = con.cursor()

    res = cur.execute(
        f""" SELECT SUM(SUM) FROM income WHERE  strftime('%m',DATE)='08';  """
    )
    res = res.fetchall()
    con.close()
    return res

def get_sum_September():
    con = sqlite3.connect('date.db')
    cur = con.cursor()

    res = cur.execute(
        f""" SELECT SUM(SUM) FROM income WHERE  strftime('%m',DATE)='09';  """
    )
    res = res.fetchall()
    con.close()
    return res


def get_sum_ex():
    con = sqlite3.connect('date.db')
    cur = con.cursor()

    res = cur.execute(
        f""" SELECT SUM(SUM) FROM expenses; """
    )
    res = res.fetchall()
    con.close()
    return res

def get_sum_ex2():
    con = sqlite3.connect('date.db')
    cur = con.cursor()

    res = cur.execute(
        f""" SELECT INCOME, SUM(SUM) as sum FROM expenses GROUP BY INCOME; """
    )
    res = res.fetchall()
    con.close()
    return res

def get_sum_ех_August():
    con = sqlite3.connect('date.db')
    cur = con.cursor()

    res = cur.execute(
        f""" SELECT SUM(SUM) FROM expenses WHERE  strftime('%m',DATE)='08';  """
    )
    res = res.fetchall()
    con.close()
    return res



# if __name__ == "__main__":


