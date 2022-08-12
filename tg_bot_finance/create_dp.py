if __name__ == "__main__":
    import sqlite3

    con = sqlite3.connect('date.db')

    cur = con.cursor()
    cur.execute(
        """
        CREATE TABLE income 
        (
        DATE text,
        INCOME text,
        SUM int
        )
        """
    )
    con.close()


    con = sqlite3.connect('date.db')

    cur = con.cursor()
    cur.execute(
        """
        CREATE TABLE expenses 
        (
        DATE text,
        EXPENSE text,
        SUM int
        )
        """
    )
    con.close()