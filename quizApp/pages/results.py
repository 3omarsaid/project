# student table

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
db = init_db.dbIns

query = """
select e.title,u.userName, a.score from attempts a
join exams e on e.ExID = a.Exid
join users u on u.Uid = a.Tchid
"""
params = ()
result =db.query(query,params)
st.write(result)