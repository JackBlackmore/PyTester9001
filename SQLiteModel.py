import sqlite3
import sys
import traceback

class SQLiteModel():
    def __init__(self, filepath):
        self.conn = self.connect(filepath)

    def connect(self, filepath):
        return sqlite3.connect(filepath)

    def modulelist(self):
        curr = self.conn.cursor()
        curr.execute("SELECT DISTINCT Module FROM QA")
        modules = [str(x[0]) for x in curr.fetchall()]
        curr.close()
        return modules

    def partlist(self, mod: str):
        try:
            curr = self.conn.cursor()
            curr.execute("SELECT DISTINCT Part FROM QA WHERE UPPER(Module) = '{0}' "
                         "ORDER BY Part".format(mod.upper()))

            parts = [str(x[0]) for x in curr.fetchall()]

        except Exception:
            curr.close()
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exc(exc_type, exc_value, exc_traceback)

        return parts

    def chapterlist(self, mod: str, part: str):
        try:
            curr = self.conn.cursor()
            curr.execute(
                "SELECT DISTINCT Chapter FROM QA where UPPER(Module) = '{0}' AND Part = {1} ORDER BY  Chapter".format(
                    mod.upper(), part))
            chapter = [str(x[0]) for x in curr.fetchall()]
        except Exception:
            curr.close()
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exc(exc_type, exc_value, exc_traceback)

        return chapter
