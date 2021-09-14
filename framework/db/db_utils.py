import sqlite3
from framework.db.scripts_for_db import ScriptForBd
import os

class ForDb(object):
    db_name = ''
    conn = ''

    def connect_for_db(self):
        self.conn = sqlite3.connect(self.db_name)

    def return_dictionary_list(self, request_for_db):
        dictionaire = {}
        keylist = []
        result_list = []
        dictionaire_list = []
        cur = self.conn.cursor()
        cur.execute(ScriptForBd.create_table_users)
        cur.execute(ScriptForBd.add_user)
        cur.execute(request_for_db)
        colnames = cur.description
        for i in range(0, len(colnames)):
            keylist.append(colnames[i][0])
        for i in range(0, len(keylist)):
            for row in cur.execute(ScriptForBd.select_from_users):
                result_list.append(row[i])
            dictionaire[keylist[i]] = result_list
            dictionaire_list.append(dictionaire)
            dictionaire = {}
            result_list = []
        os.remove(self.db_name)
        if dictionaire_list != None:
            return (dictionaire_list)
