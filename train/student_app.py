# import sqlite3

# class studentdb:
#     def __init__(self,dbname = "students.db"):
#         self.conn = sqlite3.connect(dbname)
#         self.cursor = self.conn.cursor()
#         self.createTable()
#     def createTable(self):
#         self.cursor.execute("""
#         CREATE TABLE IF NOT EXISTS students(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             name TEXT,
#             age INTEGER,
#             degrees INTEGER)
#         """)
#     def add_student(self,name,age,degrees):
#         self.cursor.execute("""
#         insert into students(name,age,degrees)
#             values(?,?,?)
#         """,(name, age, degrees))
#         self.conn.commit()
#     def add_students(self, data):
#         self.cursor.executemany("""
#         insert into students(name,age,degrees)
#             values(?,?,?)
#         """,data)
#         self.conn.commit()
#     def showAllStudents(self):
#         self.cursor.execute("""
#         select * from students
#         """)
#         return self.cursor.fetchall()
#     def deletestu(self,id):
#         self.cursor.execute("""delete from students where id = ?""",(id,))
#         self.conn.commit()
#     def searchofstu(self,id):
#         self.cursor.execute("""select * from students where id = ?""",(id,))
#         return self.cursor.fetchall()
#     def update_student(self,id,name,age,degrees):
#         self.cursor.execute("""update students
#                             set name = ?, age = ?, degrees = ?
#                             where id = ?""",(name,age,degrees,id))
#         self.conn.commit()
#     def delall(self):
#         self.cursor.execute("""delete from students""")
#         self.conn.commit()
        
#     def closeconn(self):
#         self.conn.close()
# dbstudent = studentdb()
# # dbstudent.add_student("omar", 30, 90)
# # dbstudent.delall()
# # dbstudent.deletestu(10)
# # print(dbstudent.searchofstu(3))

# data = [("omar",19,90),("mohamed",20,90)]
# data.append(("omar",19,90))
# data.append(("omar",19,90))
# dbstudent.add_students(data)
# print(dbstudent.showAllStudents())
# dbstudent.update_student(3,"momen", 20 ,60)
# print(dbstudent.showAllStudents())

# dbstudent.delall()
dec = {"name":"omar","id":1}
dec2 = {"degree": 30}
