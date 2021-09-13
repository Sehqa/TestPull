class ScriptForBd:
    create_table_users="""CREATE TABLE IF NOT EXISTS users(
               userid INT PRIMARY KEY,
               fname TEXT,
               lname TEXT,
               gender TEXT);
            """
    select_from_users="""SELECT * FROM users;"""

    add_user="""INSERT INTO users(userid, fname, lname, gender) 
   VALUES('00022', 'Alex4', 'Smith4', 'male4');"""
