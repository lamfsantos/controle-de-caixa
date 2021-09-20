import sqlite3
from sqlite3 import Error
from models.Produto import Produto 

database = r"pythonsqlite.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def find(name: str):
    conn = create_connection(database)

    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = ?", (name, picture, barCod ))

    rows = cur.fetchall()

    conn.close()

    return rows

def insert(produto: Produto):
    try:
        conn = create_connection(database)

        sql = ''' INSERT INTO users(name, )
                  VALUES(?,?,?,?,?,?) '''

        cur = conn.cursor()
        cur.execute(sql, (produto.name, produto.picture, produto.barCod))
        conn.commit()
        return cur.lastrowid
    except Exception as e:
        print(type(e))
        raise

def edit(produto: Produto):
     try:
         conn = create_connection(database)

         sql = ''' UPDATE users
                   SET picture = ?, barCod = ?
                   WHERE name = ?
                '''

         cur = conn.cursor()
         cur.execute(sql, ( produto.name, produto.picture, produto.barCod))
         conn.commit()
         return cur.lastrowid
     except Exception as e:
         print(type(e))
         raise

def deletar(produto: Produto):
  try:
      conn = create_connection(database)

      sql = "DELETE FROM users WHERE name=?"

      cur = conn.cursor()
      name = produto.name
      cur.execute(sql, (name,))
      conn.commit()
      return cur.lastrowid
  except Exception as e:
      print(type(e))
      raise
