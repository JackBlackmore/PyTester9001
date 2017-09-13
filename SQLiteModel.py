import sqlite3


class SQLiteModel():

    def __init__(self,filepath):
        self.conn = self.connect(filepath)

    def connect(self, filepath):

        return sqlite3.connect(filepath)


    def modulelist(self):
        curr = self.conn.cursor()
        curr.execute("SELECT DISTINCT MODULE FROM QA")
        modules = [str(x[0]) for x in curr.fetchall()]
        curr.close()
        return modules


