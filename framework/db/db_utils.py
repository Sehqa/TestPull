import sqlite3
from framework.db.scripts_for_db import ScriptForBd


class ForDb(object):
    db_name=''

    def dict_from_db(self,zapr):
        dict1 = {}
        keylist = []
        resultlist = []
        dictlist = []
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute(ScriptForBd.create_table_users)
        conn.commit()
        cur.execute(zapr)
        colnames = cur.description
        for i in range(0, len(colnames)):
            keylist.append(colnames[i][0])

        for i in range(0, len(keylist)):
            for row in cur.execute(ScriptForBd.select_from_users):
                resultlist.append(row[i])
            dict1[keylist[i]] = resultlist
            dictlist.append(dict1)
            dict1 = {}
            resultlist = []
        return (dictlist)
