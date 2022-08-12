import sqlite3
from datetime import datetime

DATE = datetime.now().date()

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
            (DATE, EXPENSE, SUM)
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


def get_sum_inc():
    con = sqlite3.connect('date.db')
    cur = con.cursor()

    res = cur.execute(
        f""" SELECT SUM(SUM) FROM income; """
    )
    res = res.fetchall()
    con.close()
    return res


def get_sum1_inc():
    con = sqlite3.connect('date.db')
    cur = con.cursor()

    res = cur.execute(
        f""" SELECT SUM(SUM) FROM income WHERE INCOME='Зарплата'; """
    )
    res = res.fetchall()
    con.close()
    return res

def get_sum2_inc():
    con = sqlite3.connect('date.db')
    cur = con.cursor()

    res = cur.execute(
        f""" SELECT SUM(SUM) FROM income WHERE INCOME='Перевод'; """
    )
    res = res.fetchall()
    con.close()
    return res


def get_sum_inc_month():
    con = sqlite3.connect('date.db')
    cur = con.cursor()

    res = cur.execute(
        f""" SELECT SUM(SUM) FROM income WHERE   strftime('%m',DATE)='{str(datetime.now().month).zfill(2)}';  """
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
        f""" SELECT EXPENSE, SUM(SUM) as sum FROM expenses GROUP BY EXPENSE; """
    )
    res = res.fetchall()
    con.close()
    return res

def get_sum_month():
    con = sqlite3.connect('date.db')
    cur = con.cursor()

    res = cur.execute(
        f""" SELECT SUM(SUM) FROM expenses WHERE strftime('%m',DATE)='{str(datetime.now().month).zfill(2)}';  """
    )
    res = res.fetchall()
    con.close()
    return res

