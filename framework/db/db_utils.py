import sqlite3
from framework.db.scripts_for_db import ScriptForBd


class ForDb(object):
    db_name=''
    conn=''


    def connect_for_db(self):
        self.conn = sqlite3.connect(self.db_name)

    def dict_from_db(self,request_for_db):
        dict1 = {}
        keylist = []
        resultlist = []
        dictlist = []
        cur = self.conn.cursor()
        cur.execute(request_for_db)
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
        if dictlist!=None:
            return (dictlist)
