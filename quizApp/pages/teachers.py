import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import streamlit as st
from quizApp.dataBase import init_db
db = init_db.dbIns
st.title("teacers")

teachers = db.get("users",{"role":"teacher"})
st.table(teachers)
for teacher in teachers:
    with st.container():
        col1,col2 = st.columns([1,1])
        with col1:
            st.write(teacher[1])
        with col2:
            if st.button("select",key=teacher[0]):
                st.session_state["teacherIdSelected"] = teacher[0]
                st.success(f"teacher {teacher[1]} selected")
                st.switch_page("pages/exams.py")
    st.divider()