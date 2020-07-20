import sqlite3

conn = sqlite3.connect('baza.db')

c = conn.cursor()


def stworz_tabele():
    c.execute("""
                CREATE TABLE IF NOT EXISTS ulubione(
                nazwa text
                )""")


def insert(nazwa):
    with conn:
        c.execute("INSERT INTO ulubione VALUES (:nazwa)", {'nazwa': nazwa})

def getulubione():
    c.execute("SELECT nazwa FROM ulubione")
    temp = c.fetchall()
    tab = []
    for i in temp:
        slowo = ''.join(i)
        tab.append(slowo)
    return tab

def usun(nazwa):
    with conn:
        c.execute("DELETE FROM ulubione WHERE nazwa=:nazwa",{'nazwa':nazwa})


stworz_tabele()


