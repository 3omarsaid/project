from ..dataBase import init_db
init_db.createTables()
db = init_db.dbIns
# exam = {"TchID":2 ,
#                 "title" :"exam 1",
#                 "timerType" :"qustion",
#                 "time_S" :30}
# exam2 = {"TchID":2 ,
#                 "title" :"exam 2",
#                 "timerType" :"qustion",
#                 "time_S" :30}
# exam3 = {"TchID":1 ,
#                 "title" :"exam 3",
#                 "timerType" :"qustion",
#                 "time_S" :60}
# updated_exam3 = {"TchID":1 ,
#                 "title" :"exam 3",
#                 "timerType" :"exam",
#                 "time_S" :60*60}
# teacher = {
#     "userName" : "mohammed",
#     "password" : "mohammed1234",
#     "role" : "teacher"
# }
# db.insert("users",teacher)
# db.insert("exams",exam)
# db.insert("exams",exam2)
# db.insert("exams",exam3)
# print("all exams : ",db.getAll("exams"))
# print("exam id = 1 :",db.get("exams",{"ExID":1}))
# print("exams for teacher id = 2",db.get("exams",{"TchID":2}))

# db.update("exams",updated_exam3,{"ExID":3})
# print("all exams after update Exam 3 : ",db.getAll("exams"))

# db.delete("exams",{"ExID":1})
# print("all exams after delete Exam 1 : ",db.getAll("exams"))

# بيجيب الامتحانات الي عملها المدرس الفلاني ويجيب اسمه جنب كل امتحان
# db.insert("exams",{"TchID":1 ,
#                 "title" :"exam 4",
#                 "timerType" :"qustion",
#                 "time_S" :60})
query = f""" select exams.*,users.userName,users.role from exams
join users on users.Uid = exams.TchID
where exams.TchId = ?
"""
params = (1,)
print("result of query : ",db.query(query,params))
db.insert("users",{"userName":"teacher 2","password": "1234","role":"teacher"})
# db.insert("users",{"userName":"teacher 2","password": "1233","role":"teacher"})
# db.insert("users",{"userName":"teacher 3","password": "1232","role":"teacher"})
# print(db.getAll("users"))
#``