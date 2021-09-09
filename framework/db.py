import sqlite3

class Db(object):
    db_name=''

    def dictfrombd(self,zapr):
        dict1 = {}
        keylist = []
        resultlist = []
        dictlist = []
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS users(
               userid INT PRIMARY KEY,
               fname TEXT,
               lname TEXT,
               gender TEXT);
            """)
        conn.commit()

        cur.execute(zapr)
        colnames = cur.description
        for i in range(0, len(colnames)):
            keylist.append(colnames[i][0])

        for i in range(0, len(keylist)):
            for row in cur.execute('SELECT * FROM users;'):
                resultlist.append(row[i])
            dict1[keylist[i]] = resultlist
            dictlist.append(dict1)
            dict1 = {}
            resultlist = []
        return (dictlist)
