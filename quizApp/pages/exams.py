import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
import streamlit as st
from quizApp.dataBase import init_db
db = init_db.dbIns
teacherid=2
role="teacher"
teacher=db.get("users",{"Uid":teacherid})
teachername=teacher[0][1]
st.title(teachername)
exams=db.get("exams",{"TchID":teacherid})
if role=="student":
    # student
    for exam in exams:
        st.container()
        col1,col2=st.columns([3,1])
        with col1:
            st.write(exam[2])
        with col2:
            if st.button("select",key=exam[0]):
                st.session_state.action="select"
                st.session_state.exid=exam[0]
                st.switch_page("pages/qustions.py")
else:
    #teacher
    for exam in exams:
        with st.container():
            col1,col2=st.columns([3,1])
            with col1:
                st.write(exam[2])
            with col2:
                with st.container():
                    col1,col2=st.columns([1,1])
                    with col1:
                        if st.button("Edit",key=f"Edit_{exam[0]}"):
                            st.session_state.action="Edit"
                            st.session_state.exid=exam[0]
                            st.switch_page("pages/qustions.py") 
                    with col2:
                        if st.button("Delete",key=f"Del_{exam[0]}"):
                            db.delete("exams",{"ExID":exam[0]})
    if st.button("Create"):
        st.session_state.action="Create"
        st.switch_page("pages/qustions.py")


