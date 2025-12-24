import sys
import os
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import streamlit as st
import time
from quizApp.dataBase import init_db
from pages.timer_exams import Qus_countdown_timer,exam_timer_autoupdate

db = init_db.dbIns

exid= st.session_state["exid"]
tchid = st.session_state["teacher_id"]
stuid = st.session_state.userID
qustions = db.get("qustions",{"ExID":exid})

if "index" not in st.session_state:
    st.session_state.index = 0
index = st.session_state.index
if "score" not in st.session_state:
    st.session_state.score = 0
score = st.session_state.score
if "attid" not in st.session_state:
    exam=db.get("exams", {"ExID":exid})[0]
    st.session_state.examObj = exam
    attid=db.insert("attempts", {"ExID":exid , "StuID":stuid , "TchID":tchid , "score":0 , "duration_S":0, "numQus":exam[5], "total_time":exam[4] if exam[3] == "exam" else exam[4] * exam[5]})
    st.session_state.attid = attid
attid = st.session_state.attid
exam = st.session_state.examObj
if(exam[3] == "exam"):
    exam_timer_autoupdate(exam[4])
    if st.session_state.get("exam_finished"):
            st.warning("exam ended")
            del st.session_state.exam_start
            st.session_state.index = len(qustions)
            st.stop()
if index == len(qustions):
    att=db.get("attempts", {"AttID":attid})[0]
    start_at = datetime.strptime(att[4], "%Y-%m-%d %H:%M:%S")
    dur=datetime.now()-start_at
    newAtt={"score":score, "duration_S":int(dur.total_seconds()), "ExID":att[1],"StuID":att[2] , "TchID":att[3], "numQus":att[6], "start_at":att[4], "total_time":att[8] }
    db.update("attempts", newAtt, {"AttID":attid})
    st.session_state.duration = int(dur.total_seconds())
    del st.session_state.index
    st.switch_page("pages/result.py")
    st.stop()
else :
    if exam[3] == "Question":
        remain = Qus_countdown_timer(exam[4])
        if st.session_state.get("timer_done"):
            st.warning("time ended")
            del st.session_state.timer_start
            st.session_state.index = index+1
            st.rerun()
    st.title(qustions[index][2])
    choices = db.get("choices", {"QusID":qustions[index][0]})
    for choice in choices:
        choiceHeader=choice[2]
        if st.button(choiceHeader):
            db.insert("answers", {"QusID":qustions[index][0], "AttID": attid, "ChID":choice[0], "correctnes":choice[3]})
            st.session_state.score =score+choice[3]
            st.session_state.index = index+1
            if "timer_start" in st.session_state:
                del st.session_state.timer_start
            st.rerun()
time.sleep(1)
st.rerun()