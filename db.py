import os
import sqlite3

def initDB(DATABASE):
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        create_table_sql = """ CREATE TABLE IF NOT EXISTS device (
                                            id integer PRIMARY KEY,
                                            IP text NOT NULL,
                                            MAC text,
                                            Device text,
                                            Status text,
                                            currenttime text
                                        ); """
        cur.execute(create_table_sql)
        conn.commit()
        create_table_sql2 = """ CREATE TABLE IF NOT EXISTS attack (
                                                    id integer PRIMARY KEY,
                                                    devies integer,
                                                    attacks integer
                                                ); """
        cur.execute(create_table_sql2)
        conn.commit()

        sql = ''' INSERT INTO attack(id,devies,attacks)
                          VALUES(?,?,?) '''
        i = 1
        c = 0
        a = 0
        data = (i, c, a)
        cur.execute(sql, data)
        conn.commit()