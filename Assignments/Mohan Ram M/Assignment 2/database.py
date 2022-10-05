import sqlite3 as sql
defretrieveUsers():
    con = sql.connect("User_database.db")
    cur = con.cursor()
    cur.execute("SELECT username, pin FROM users")
    users = cur.fetchone()
    con.close()
    return users

