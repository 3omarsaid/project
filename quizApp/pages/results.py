# attempts table
# student name
# Exam Title
# teacher name
# Score
# numQus
# Duration
# total time
# Attempt Date
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import streamlit as st
from quizApp.dataBase import init_db
import pandas as pd
db = init_db.dbIns
role = "student"
if role == "teacher":
    where = "a.TchID"
    name = "Stu"
    tchid= 2
    params = (tchid,)
else:
    where = "a.StuID"
    name = "Tch"
    stuid = 3
    params = (stuid,)
query = f"""
select {name}.userName, e.title, a.score,a.numQus,a.duration_S,a.total_time,a.start_at from attempts a
join exams e on e.ExID = a.Exid
join users Tch on Tch.Uid = a.Tchid
join users Stu on Stu.Uid = a.StuID
where {where} = ?
"""

result =db.query(query,params)
df=pd.DataFrame(result,columns=[ 'student name'if name == "Stu" else 'teacher name' ,'Exam Title','Score','numQus','Duration','total time','Attempt Date'])
st.dataframe(df)