import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"pythonsqlite.db"

    sql_create_cadastro_table = """ CREATE TABLE IF NOT EXISTS produtos (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        picture text NOT NULL,
                                        barCod text NOT NULL
                                    ); """

    # sql_create_fodase_table = """ CREATE TABLE IF NOT EXISTS fodase (
    #                                     id integer PRIMARY KEY,
    #                                     username text NOT NULL,
    #                                     balance real NOT NULL,
    #                                     disabled BOOLEAN NOT NULL CHECK (disabled IN (0,1))
    #                                 ); """

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_cadastro_table)
        # create_table(conn, sql_create_fodase_table)

    else:
        print("Error! Impossible to establish connection to db.")


if __name__ == '__main__':
    main()
