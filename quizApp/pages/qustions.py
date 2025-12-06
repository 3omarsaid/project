import sys
import os
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import streamlit as st
from quizApp.dataBase import init_db
db = init_db.dbIns
exid= st.session_state["exid"]
tchid = 2
stuid = 1
# st.write(st.session_state.action)
qustions = db.get("qustions",{"ExID":exid})
if "index" not in st.session_state:
    st.session_state.index = 0
index = st.session_state.index
if "score" not in st.session_state:
    st.session_state.score = 0
score = st.session_state.score
if "attid" not in st.session_state:
    exam=db.get("exams", {"ExID":exid})[0]
    attid=db.insert("attempts", {"ExID":exid , "StuID":stuid , "TchID":tchid , "score":0 , "duration_S":0, "numQus":exam[5], "total_time":exam[4] if exam[3] == "exam" else exam[4] * exam[5]})
    st.session_state.attid = attid
attid = st.session_state.attid
if index == len(qustions):
    att=db.get("attempts", {"AttID":attid})[0]
    start_at = datetime.strptime(att[4], "%Y-%m-%d %H:%M:%S")
    dur=datetime.now()-start_at
    newAtt={"score":score, "duration_S":int(dur.total_seconds()), "ExID":att[1],"StuID":att[2] , "TchID":att[3], "numQus":att[6], "start_at":att[4], "total_time":att[8] }
    db.update("attempts", newAtt, {"AttID":attid})
    st.success(score)
else :
    st.title(qustions[index][2])

    choices = db.get("choices", {"QusID":qustions[index][0]})
    for choice in choices:
        choiceHeader=choice[2]
        if st.button(choiceHeader):
            db.insert("answers", {"QusID":qustions[index][0], "AttID": attid, "ChID":choice[0], "correctnes":choice[3]})
            st.session_state.score =score+choice[3]
            st.session_state.index = index+1
            st.rerun()
       