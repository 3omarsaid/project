import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import streamlit as st
from quizApp.dataBase import init_db
db = init_db.dbIns

exmid = st.session_state.exid
if "exam" not in st.session_state:
    st.session_state.exam = db.get("exams",{"ExID":exmid})[0]
exam = st.session_state.exam
if "qustions" not in st.session_state:
    st.session_state.qustions=db.get("qustions",{"ExID":exmid})
qustions=st.session_state.qustions
title=st.text_input("title",placeholder="enter the title of the exam",value=exam[2])
typeOptions = ["Question","exam"]
timertype=st.radio("timer type",typeOptions,index=typeOptions.index(exam[3]))
timeinmin=st.number_input("time in minutes",value=exam[4]/60)
if st.button("update exam"):
    db.update("exams",{"TchID":2,"title":title,"timerType":timertype,"time_s":timeinmin*60},{"ExID":exmid})
qus={}
choices = []
def creation(indx,oldChoices):
    global qus
    global choices
    header=st.text_input("header",placeholder="enter your qestion ",key=f"header{indx}",value=qustions[indx][2])
    with st.container():
        col1,col2 = st.columns([1,1])
        with col1:
            ch1=st.text_input("choose 1",placeholder="enter your choose ",key=f"ch1{indx}",value=oldChoices[0][2])
            ch2=st.text_input("choose 2",placeholder="enter your choose ",key=f"ch2{indx}",value=oldChoices[1][2])
        with col2:
            ch3=st.text_input("choose 3",placeholder="enter your choose ",key=f"ch3{indx}",value=oldChoices[2][2])
            ch4=st.text_input("choose 4",placeholder="enter your choose ",key=f"ch4{indx}",value=oldChoices[3][2])
    correctindx = 0
    qusid = qustions[indx][0]
    for choice in oldChoices:
        if choice[3]:
            break
        correctindx+=1
    correct=st.selectbox("correct choice",[ch1,ch2,ch3,ch4],key=f"correct{indx}",index=correctindx)
    if st.button("Update",key=f"update{indx}"):
        qus={"ExID":st.session_state.exmid,"header":header}
        choices=[{"text":ch1,"correct":correct==ch1},
                    {"text":ch2,"correct":correct==ch2},
                    {"text":ch3,"correct":correct==ch3},
                    {"text":ch4,"correct":correct==ch4},]
        
        db.update("qustions",qus,{"QusID":qusid})
        db.delete("choices", {"QusID": qusid})
        for cho in choices:
            cho["QusID"] = qusid
        db.insertMany("choices", choices)
        st.rerun()
    if st.button("delete",key=f"del{indx}"):
        db.delete("qustions",{"QusID":qusid})
        db.delete("choices",{"QusID":qusid})
        st.session_state.pop("qustions")
        st.rerun()
    st.write("-------------------------------")
    
for i in range(len(qustions)):
    oldchoices = db.get("choices",{"QusID":qustions[i][0]})
    creation(i,oldchoices)
sub=st.button("submit")

if sub:
    db.update("exams",{"TchID":2,"title":title,"timerType":timertype,"time_s":timeinmin*60,"numQus":len(qustions)},{"ExID":exmid})
    st.session_state.clear()
    st.switch_page("pages/exams.py")
    