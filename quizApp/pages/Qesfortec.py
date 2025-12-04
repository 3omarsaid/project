import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import streamlit as st
from quizApp.dataBase import init_db
db = init_db.dbIns
title=st.text_input("title",placeholder="enter the title of the exam")
timertype=st.radio("timeer type",["Question","exam"])
timeinmin=st.number_input("time in minutes")
if "count" not in st.session_state:
    st.session_state.count=0
if "exmid" not in st.session_state:
    st.session_state.exmid = None
if st.button("create exam"):
    st.session_state.exmid =db.insert("exams",{"TchID":2,"title":title,"timerType":timertype,"time_s":timeinmin*60})
    st.write(st.session_state.exmid)
if st.session_state.exmid:
    qus={}
    choices = []
    def creation(indx):
        global qus
        global choices
        header=st.text_input("header",placeholder="enter your qestion ",key=f"header{indx}")
        ch1=st.text_input("choose 1",placeholder="enter your choose ",key=f"ch1{indx}")
        ch2=st.text_input("choose 2",placeholder="enter your choose ",key=f"ch2{indx}")
        ch3=st.text_input("choose 3",placeholder="enter your choose ",key=f"ch3{indx}")
        ch4=st.text_input("choose 4",placeholder="enter your choose ",key=f"ch4{indx}")
        correct=st.selectbox("correct choice",[ch1,ch2,ch3,ch4])
        st.write("-------------------------------")
        if i==st.session_state.count:
            qus={"ExID":st.session_state.exmid,"header":header}
            choices=[{"text":ch1,"correct":correct==ch1},
                        {"text":ch2,"correct":correct==ch2},
                        {"text":ch3,"correct":correct==ch3},
                        {"text":ch4,"correct":correct==ch4},]
    for i in range(st.session_state.count+1):
        creation(i)
    sub=st.button("submit")
    add=st.button("Add anthor Qestion")
    if add:
        qusid = db.insert("qustions",qus)
        for cho in choices:
            cho["QusID"] = qusid
        db.insertMany("choices",choices)
        st.session_state.count+=1
        st.rerun()

    if sub:
        qusid = db.insert("qustions",qus)
        for cho in choices:
            cho["QusID"] = qusid
        db.insertMany("choices",choices)
        st.session_state.clear()
        st.switch_page("pages/exams.py")







