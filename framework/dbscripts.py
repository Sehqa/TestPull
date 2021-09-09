class script_for_bd:
    create_table_users="""CREATE TABLE IF NOT EXISTS users(
               userid INT PRIMARY KEY,
               fname TEXT,
               lname TEXT,
               gender TEXT);
            """
    select_from_users="""SELECT * FROM users;"""