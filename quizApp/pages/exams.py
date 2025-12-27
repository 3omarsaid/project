import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import streamlit as st
from quizApp.dataBase import init_db
from quizApp.pages.User import Student, Teacher

db = init_db.dbIns

current_user = st.session_state.get("current_user")

if not current_user:
    st.error("Please login first")
    st.switch_page("pages/authntcation.py")
    st.stop()

st.title(current_user.userName)

if isinstance(current_user, Teacher):
    exams = db.get("exams", {"TchID": current_user.Uid})
else:
    teacher_id = st.session_state.get("teacher_id")
    if teacher_id:
        exams = db.get("exams", {"TchID": teacher_id})

if isinstance(current_user, Student):
    # Student view
    for exam in exams:
        st.container()
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"### {exam[2]}")
        with col2:
            if st.button("select", key=exam[0]):
                st.session_state.exid = exam[0]
                st.switch_page("pages/qustions.py")
    if st.button("results"):
        st.switch_page("pages/results.py")
    if st.button("results"):
        st.switch_page("pages/teachers.py")
else:
    # teacher view
    for exam in exams:
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(exam[2])
            with col2:
                with st.container():
                    col1, col2 = st.columns([1, 1])
                    with col1:
                        if st.button("Edit", key=f"Edit_{exam[0]}"):
                            st.session_state.exid = exam[0]
                            st.switch_page("pages/editQest.py") 
                    with col2:
                        if st.button("Delete", key=f"Del_{exam[0]}"):
                            db.delete("exams", {"ExID": exam[0]})
    if st.button("Create"):
        st.switch_page("pages/Qesfortec.py")
    if st.button("results"):
        st.switch_page("pages/results.py")