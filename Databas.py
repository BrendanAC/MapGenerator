import sqlite3
import sys
import os
from contextlib import closing



class DB:


    def __init__(self):
        self.conn=None
        self.conn=self.connect()




    def connect(self):
        if not self.conn:
            if sys.platform == "win32":
                DB_FILE = "C:\\Users\\wishbone561\\Downloads\\Program\\MapGenerator\\Maps.sqlite"
            else:
                HOME = os.environ["HOME"]
                DB_FILE = HOME + "C:\\Users\\wishbone561\\Downloads\\Program\\MapGenerator\\Maps.sqlite"

            conn = sqlite3.connect(DB_FILE)
            conn.row_factory = sqlite3.Row

        return self.conn

    def add_map(map):
        sql='''INSERT'''
    def close(self):
        if self.conn:
            self.conn.close()
