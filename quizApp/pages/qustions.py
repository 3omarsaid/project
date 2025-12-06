import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import streamlit as st
from quizApp.dataBase import init_db
db = init_db.dbIns
exid= st.session_state["exid"]
tchid = 2
stuid = 1
# st.write(st.session_state.action)
qustions = db.get("qustions",{"ExID":exid})
st.write(qustions)
if "index" not in st.session_state:
    st.session_state.index = 0
index = st.session_state.index
if "score" not in st.session_state:
    st.session_state.score = 0
score = st.session_state.score
if "attid" not in st.session_state:
    attid=db.insert("attempts", {"ExID":exid , "StuID":stuid , "TchID":tchid , "score":0 , "duration_S":0})
    st.session_state.attid = attid
attid = st.session_state.attid
if index == len(qustions):
    att=db.get("attempts", {"AttID":attid})
    st.write(att)
    # newAtt={"ExID":att[1] , "StuID":stuid , "TchID":tchid , "score":0 , "duration_S":0}
    st.write(score)
else :
    st.title(qustions[index][2])

    choices = db.get("choices", {"QusID":qustions[index][0]})
    for choice in choices:
        choiceHeader=choice[2]
        if st.button(choiceHeader):
            st.session_state.score =score+choice[3]
            st.session_state.index = index+1
            st.rerun()
       