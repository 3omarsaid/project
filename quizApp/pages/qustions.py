import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import streamlit as st
from quizApp.dataBase import init_db
db = init_db.dbIns
exid= st.session_state["exid"]
# st.write(st.session_state.action)
qustions = db.get("qustions",{"ExID":exid})
if "index" not in st.session_state:
    st.session_state.index = 0
index = st.session_state.index
st.title(qustions[index][2])
choices = db.get("choices",{"QusID":qustions[index][0]})
st.write(choices)
if st.button("next"):
    st.session_state.index = index+1
    st.rerun()