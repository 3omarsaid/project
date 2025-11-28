import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import streamlit as st
from quizApp.dataBase import init_db
db = init_db.dbIns
title=st.text_input("title",placeholder="enter the title of the exam")
timertype=st.radio("timeer type",["Question","exam"])
timeinmin=st.number_input("time in minutes")
if st.button("create exam"):
    exmId=db.insert("exams",{"TchID":2,"title":title,"timerType":timertype,"time_s":timeinmin*60})

if "questions" not in st.session_state:
    st.session_state.questions=[]
qus={}
def creation(indx):
    global qus
    header=st.text_input("header",placeholder="enter your qestion ",key=f"header{indx}")
    ch1=st.text_input("choose 1",placeholder="enter your choose ",key=f"ch1{indx}")
    ch2=st.text_input("choose 2",placeholder="enter your choose ",key=f"ch2{indx}")
    ch3=st.text_input("choose 3",placeholder="enter your choose ",key=f"ch3{indx}")
    ch4=st.text_input("choose 4",placeholder="enter your choose ",key=f"ch4{indx}")
    st.write("-------------------------------")
    if i==len(st.session_state.questions):
       qus={"ExID":exmId,"header":header}
       choices={}
for i in range(len(st.session_state.questions)+1):
     creation(i)
sub=st.button("submit")
add=st.button("Add anthor Qestion")
if add:
   st.session_state.questions.append(qus)
   st.rerun()

if sub:   
    st.session_state.clear()
    st.rerun()

st.write(st.session_state.get("questions","no questions"))
    



