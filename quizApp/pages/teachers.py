import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import streamlit as st
from quizApp.dataBase import init_db
db = init_db.dbIns

st.title("teacers")

teachers = db.get("users",{"role":"teacher"})
for teacher in teachers:
    with st.container():
        col1,col2 = st.columns([2,1])
        with col1:
            st.markdown(f"### {teacher[1]}")
        with col2:
            if st.button("select",key=teacher[0]):
                st.session_state["teacher_id"] = teacher[0]
                st.success(f"teacher {teacher[1]} selected")
                st.switch_page("pages/exams.py")
    st.divider()