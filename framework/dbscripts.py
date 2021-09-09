class script_for_bd:
    script1="""CREATE TABLE IF NOT EXISTS users(
               userid INT PRIMARY KEY,
               fname TEXT,
               lname TEXT,
               gender TEXT);
            """