import sqlite3
# CRUD all tables
# create - read - update - delete
class dbManager:
    def __init__(self,path = "quiz.db"):
        self.path = path
    def connect(self):
        conn = sqlite3.connect(self.path)
        conn.execute("pragma forign_keys = on;")
        return conn
    def insert(self,table,row:dict):
        conn = self.connect()
        curs = conn.cursor()
        keys = ','.join(row.keys())
        placeholders = ','.join(['?']*len(row))
        params = tuple(row.values())
        curs.execute(f"""insert into {table}({keys})
                    values({placeholders})""",params)
        conn.commit()
    def getAll(self,table):
        conn = self.connect()
        curs = conn.cursor()
        return curs.execute(f"select * from {table}").fetchall()
    def get(self,table,where : dict):
        key = list(where.keys())[0]
        val = list(where.values())[0]
        conn = self.connect()
        curs = conn.cursor()
        return curs.execute(f"select * from {table} where {key} = ?",(val,)).fetchall()
    def delete(self,table,where : dict):
        key = list(where.keys())[0]
        val = list(where.values())[0]
        conn = self.connect()
        curs = conn.cursor()
        curs.execute(f"delete from {table} where {key} = ?",(val,))
        conn.commit()
    def update(self,table,row:dict,where:dict):
        conn = self.connect()
        curs = conn.cursor()
        key = list(where.keys())[0]
        keys = ' = ? ,'.join(row.keys())+' = ? '
        params = tuple(list(row.values())+list(where.values()))
        curs.execute(f"""update {table} set {keys} where {key} = ?""",params)
        conn.commit()
    def query(self,query,params:tuple):
        conn = self.connect()
        curs = conn.cursor()
        curs.execute(query,params)
        conn.commit()
        return curs.fetchall()