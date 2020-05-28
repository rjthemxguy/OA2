
from os import system
from colorama import Fore, Back, Style
import time
import sqlite3


class database_class:
    def __init__(self):

        try:
            self.conn = sqlite3.connect("db/vernon.db")
        except sqlite3.Error as e:
            print(e)
            print("Database Error")
            exit(1)

    def getCPT(self, emgCode):
        self.code = emgCode

        cur = self.conn.cursor()
        cur.execute("SELECT CPT FROM codes WHERE code=?", (self.code,))

        rows = cur.fetchall()

        return rows[0]

    def getPrice(self, CPT):

        cur = self.conn.cursor()
        cur.execute("SELECT price FROM comp WHERE hcpcs=? LIMIT 1", (CPT,))

        rows = cur.fetchone()

        if len(rows) == 1:
            price = rows[0]

        else:
            price = rows

        return price







